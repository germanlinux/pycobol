from dataclasses import dataclass, field

from comportement  import Comportement
#from parser_cobol import *
#from typing import ClassVar
#from inspect import *
#from zonage import *
from arbrezone import ArbreZone
#################################
#   classe ZoneGroupe           #
#################################


@dataclass
class ZoneGroupe:
    ''' Cette classe prend en charge la creation d'une zone groupe. 
    Par nature cette zone est de type ALN.
    Sa longueur est la somme des longueurs des composants qui la composent
    
    >>> obj = ZoneGroupe('zoneessai', 1, 0)
    >>> obj.nom
    'zoneessai'
    >>> objfils = ZoneGroupe('zonefils', 2)
    >>> obj.ajout_fils_groupe(objfils)
    >>> len(obj.fils)
    1
    >>> from zonesimple import *
    >>> objfilsimp = ZoneFilsSimple('essaifils', 5, picture = '999')
    >>> obj.ajout_fils_simple(objfilsimp)
    >>> obj.longueur_utile
    3
    >>> obj.init_groupe()
    >>> obj.move_value('ERIC')
    >>> obj.valeur_externe
    'ERI'
    >>> objfilgrp = ZoneGroupe('essaifils', 2)
    >>> objfilsimp2 = ZoneFilsSimple('essaifils2',5 , picture = '99')
    >>> objfilgrp.ajout_fils_simple(objfilsimp2)
    >>> obj.ajout_fils_simple(objfilgrp)
    >>> objfilsimp3 = ZoneFilsSimple('essaifils5',5 , picture = 'XXXXX')
    >>> obj.ajout_fils_simple(objfilsimp3)
    >>> obj.maj_longueur()
    10
    >>> obj.longueur_utile
    10
    >>> obj.init_groupe()
    '''

    nom: str
    rang : int
    pere: int = 0
    fils : list = field(default_factory=list)
    son_type: str = 'GRP'
    usage: str = 'DISPLAY'
    longueur_utile: int = 0  
    valeur_interne: str =''
    valeur_externe: str = ''
    section: str = 'NON RENSEIGNE'
    comportement_associe: object = None
    #arbreInverse :ClassVar[list] = []

    def __post_init__(self):
        arbre = ArbreZone()
        arbre.zone.append(self)

    def __str__(self):
        if self.pere == 0:
            pere = 'ROOT'
        else:
            pere = self.pere.nom    
        chaine = f"{self.nom} - {self.rang} - {pere}  {len(self.fils)}:\n"
        for item in self.fils:
            if item.son_type == 'GRP':
                chaine += f"{item.nom} - {item.rang}  {item.pere.nom}\n"
            else:
                chaine += f"{item.nom} - {item.rang}- {item.picture}\n"
        return chaine        
    
    def ajout_fils_groupe(self, other):
        if other.rang <= self.rang :
            raise RuntimeError(f'Erreur sur le rang   {self.nom} >> {other.nom}') 
        other.pere = self
        if other.nom.lower() == 'filler':
            _nom = ZoneGroupe.traite_filler(other.nom , self.nom)
            other.nom = _nom
        self.longueur_utile += other.longueur_utile
        self.fils.append(other)

    def move_to(self, other):
        ''' methode interne '''
        valeur = self.valeur_externe
        if type(other) == str :
            arbre = ArbreZone()
            other= arbre.recherche_nom(other)

        other.move_value(valeur)


    #####  Alias #####
        
    ajout_fils_simple = ajout_fils_groupe
        

    def maj_valeur(self): ### TO DO attaquer les longueurs pas les valeurs
        '''normalement tous les ajouts de zones provoquent la mise à jour de la longueur
        les zones simples sont initialisées , il faut repercuter l'init  sur les zones groupes meres
        La zone groupe doit etre parcourue: pour toute zone simple on reprendra la valeur , si c est une zone
        groupe il faut elle aussi la parcourir. L'objectif est de mettre à jour les valeurs resultantes. 
        '''
        valeur_str_ =''
        for item in self.fils:
            if item.son_type == 'GRP':
               valeur_str_ +=  item.maj_valeur()
            else:
               valeur_str_ += item.valeur_externe    
        self.valeur_externe = valeur_str_
        return self.valeur_externe
    
    def maj_longueur(self): ### TO DO attaquer les longueurs pas les valeurs
        '''normalement tous les ajouts de zones provoquent la mise à jour de la longueur
        les zones simples sont initialisées , il faut repercuter l'init  sur les zones groupes meres
        La zone groupe doit etre parcourue: pour toute zone simple on reprendra la valeur , si c est une zone
        groupe il faut elle aussi la parcourir. L'objectif est de mettre à jour les valeurs resultantes. 
        '''
        longueur_ = 0
        for item in self.fils:
            if item.son_type == 'GRP':
                longueur_ +=  item.maj_longueur()

            else:
                longueur_ += item.longueur_utile
                item.comportement_associe = Comportement(item.son_type,item.longueur_utile, None )    
        self.longueur_utile = longueur_
        self.comportement_associe = Comportement(self.son_type,self.longueur_utile, None )
        return self.longueur_utile
    
    def init_groupe(self):
        self.maj_longueur()
        self.maj_valeur()
        #comportement_ = Comportement(self.son_type , self.longueur_utile , None )

        #self.comportement_associe = comportement_

    def move_value(self, valeur):
        self.comportement_associe.move_value(self,valeur)
        self.propage(self.valeur_externe)
        self.retro_propagation()
        ### maj des zones redefine
        ### zone cible ?
        arbre = ArbreZone()
        if self.nom in arbre.inv_redefine:
            cible= arbre.inv_redefine[self.nom]
            cible.valeur_externe = self.valeur_externe
            cible.propage(cible.valeur_externe)
            cible.retro_propagation()
        ### traitement des zones redefine 
        if self.nom in arbre.redefine:
            cible= arbre.redefine[self.nom]
            cible.valeur_externe = self.valeur_externe
            cible.propage(cible.valeur_externe)
            cible.retro_propagation()
    
    def propage(self, valeur):
        for un_fils in self.fils : 
            if un_fils.son_type == 'GRP':
                valeur_= valeur[:un_fils.longueur_utile]
                un_fils.valeur_externe = valeur_
                valeur = un_fils.propage(valeur) 
            else:
                valeur_= valeur[:un_fils.longueur_utile]
                un_fils.valeur_externe = valeur_
                valeur = valeur[un_fils.longueur_utile:]
        return valeur   

    def retro_propagation(self):
        arbre = ArbreZone()
        arbre.retroArbre()
        _inverse = arbre.inverse
        if self.nom in _inverse:
            for item in _inverse[self.nom]:
                r_item = arbre.recherche_nom(item)
                r_item.maj_valeur()
                
    

    ######################
    # methodes statiques #
    ######################
    @staticmethod
    def traite_filler(filler, nom):
        '''Une zone filler peut avoir des doublons, le nom sera donc formé du nom de 
        la zone accolé  avec le nom de la structure supérieure. 
        En cas de doublon un indice est ajouté à l'ensemnle.

        :param filler: nom de la zone , a priori souvent égale à filler
        :param nom: nom de la structure supérieure
        :type filler: str
        :type nom: str

        >>> traite_filler('filler', 'sup')
        'filler_sup'
        '''

        _tmp_nom = filler + '_'  + nom
        arbre = ArbreZone()
        cp = 0
        while 1:
          tmp = arbre.recherche_nom(_tmp_nom)
          if tmp is None:
            break
          cp += 1
          _tmp_nom += f'_{str(cp)}'    
        return _tmp_nom
                    
    @staticmethod            
    def get_arbre():
        arbre = ArbreZone()
        return arbre.zone
    
    @staticmethod            
    def reset_arbre():
        arbre = ArbreZone()
        arbre.reset()    

    @staticmethod            
    def vidage():
        arbre = ArbreZone()
        return arbre.vidage()    


if __name__ == '__main__':   # pragma: no cover
    import doctest          
    

    doctest.run_docstring_examples(ZoneGroupe,None, verbose = 1)
    #doctest.run_docstring_examples(ZoneFilsSimple,None, verbose = 1)
    #doctest.run_docstring_examples(ZoneSimpleRedefine,None, verbose = 1)
    doctest.run_docstring_examples(ZoneGroupe.read_groupe_from_code,None, verbose = 1)
    #tlignes = ZoneGroupe.fake_read_file()
    #ZoneGroupe.read_groupe_from_code(tlignes)
    #doctest.run_docstring_examples(ZoneGroupe.recherche_nom,None, verbose = 1)