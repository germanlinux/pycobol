import re
from dataclasses import dataclass, field
from collections import defaultdict
from comportement  import *
from zonesimple import *
from typing import ClassVar
from inspect import *
from zonage import *
from arbrezone import *
#################################
#   classe ZoneGroupe           #
#################################


@dataclass
class ZoneGroupe():
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
    fils : list[int] = field(default_factory=list)
    son_type: str = 'GRP'
    usage: str = 'DISPLAY'
    longueur_utile: int = 0  
    valeur_interne: str =''
    valeur_externe: str = ''
    section: str = 'NON RENSEIGNE'
    comportement_associe: object = None
    arbreInverse :ClassVar[list] = []

    def __post_init__(self):
        arbre = ArbreZone()
        arbre.zone.append(self)

    def __str(self):
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
        self.longueur_utile += other.longueur_utile
        self.fils.append(other)

    def move_to(self, other):
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
        obj_valeur = Value(valeur)
        self.comportement_associe.move_value(self,valeur)
        self.propage(self.valeur_externe)
        self.retro_propagation()
    
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
        if self.nom in ZoneGroupe.arbreInverse:
            for item in ZoneGroupe.arbreInverse[self.nom]:
                print('ERRRRR' , item)
                     #item.maj_valeur()
######################
# methodes de classe #
######################


    
    
    @classmethod        
    def retroArbre():
        ''' Reconstitution des dependances des zones en partant des zones élémentaires
        
        ZoneGroupe.arbreInverse = defaultdict(list)
        for item in ZoneGroupe.zone_groupe:
            try:
                if item.fils: 
                   for _fils in item.fils:
                        ZoneGroupe.arbreInverse[_fils.nom].append(item.nom)
            except:
                pass 
         
        for cle,value  in  ZoneGroupe.arbreInverse.items():
            for _fils in value:
                 if _fils in ZoneGroupe.arbreInverse:
                        ZoneGroupe.arbreInverse[cle].extend(ZoneGroupe.arbreInverse[_fils])
                        break
        '''
        pass

######################
# methodes statiques #
######################
    @staticmethod
    def read_groupe_from_code(tcode):
        ''' cette fonction prend comme parametre en entrée un tableau de ligne
        et en fonction du contenu active un constructeur de groupe ou de zone simple
        >>> tlignes = ZoneGroupe.fake_read_file()
        >>> len(tlignes)
        4
        >>> ZoneGroupe.read_groupe_from_code(tlignes)
        >>> len(ZoneGroupe.zone_groupe[0].fils)
        3
        '''
        _zonegrp_active = ''
        _niveaux_max = 99
        ### to do : mutualiser
        for ligne in tcode:
            if ligne[-1] == '\n':
                ligne= ligne[:-1]
        
            ligne = ligne.strip()
            result = re.sub(' +', ' ', ligne)
            if result:
                tab = result.split(' ')
                if tab[-1][-1] == '.' :
                    tab[-1] = tab[-1][:-1]
            else:
                break

            if ' PIC '  in ligne  or ' PICTURE ' in ligne:
                arbre = ArbreZone()
                if len(arbre.zone) == 0:
                    niveaux_max = 0
                else: 
                    niveaux_max = arbre.zone[-1].rang    
                (type_,pic, longueur,decimale) =  Zone.traite_pic(tab)
                niv = Zone.extract_niveau(tab)
                arbre = ArbreZone()
                obt = arbre.recherche_rang(niv)
                _nom =  Zone.extract_nom(tab)
                obj_s = ZoneFilsSimple(_nom,niv ,picture = pic )
                obt.ajout_fils_simple(obj_s)
               
            else: 
                ## zone groupe
                niv = Zone.extract_niveau(tab)
                _nom =  Zone.extract_nom(tab)
                arbre = ArbreZone()
                if len(arbre.zone) == 0:
                    obj_p = ZoneGroupe(_nom, niv)
                else:
                    ### niveau inferieur
                    ###  ou niveau frere
                    arbre = ArbreZone()
                    obt = arbre.recherche_rang(niv)
                    obj_s  = ZoneGroupe(_nom, niv)
                    obt.ajout_fils_simple(obj_s)
                    
        return arbre            
                ## est ce le niveau le plus haut ?
                ##  ca peut etre une zone groupe dans une zone groupe  
    @staticmethod            
    def fake_read_file(data= None):
        zg1 ='''
                10            DAECH.                                   
                    11            AECH   PICTURE  9(4).                 
                    11            MECH   PICTURE  99.                      
                    11            JECH   PICTURE  99.                 
        '''            
        
        if not data:
          data = zg1
        t_zg1 = data.split('\n')
        lignes = [item  for item in t_zg1 if item]
        return(lignes)

    @staticmethod            
    def get_arbre():
        arbre = ArbreZone()
        return arbre.zone
        
    

if __name__ == '__main__':  
    import doctest          
    
'''
    doctest.run_docstring_examples(ZoneGroupe,None, verbose = 1)
    doctest.run_docstring_examples(ZoneFilsSimple,None, verbose = 1)
    #doctest.run_docstring_examples(ZoneSimpleRedefine,None, verbose = 1)
    #doctest.run_docstring_examples(ZoneGroupe.read_groupe_from_code,None, verbose = 1)
    #tlignes = ZoneGroupe.fake_read_file()
    #ZoneGroupe.read_groupe_from_code(tlignes)
    #doctest.run_docstring_examples(ZoneGroupe.recherche_nom,None, verbose = 1)
    '''