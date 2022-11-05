import re
from dataclasses import dataclass, field
from comportement  import *
from typing import ClassVar
from inspect import *
from zonage import *
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
    >>> objfils.pere # doctest: +ELLIPSIS
    ZoneGroupe(nom='zoneessai'...
    >>> objfils2 = ZoneGroupe('zonefils2', 1)
    >>> obj.ajout_fils_groupe(objfils2)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    >>> objfilsimp = ZoneFilsSimple('essaifils', 5, picture = '999')
    >>> obj.ajout_fils_simple(objfilsimp)
    >>> obj.longueur_utile
    3
    >>> obj.maj_valeur()
    '000'
    >>> obj.init_groupe()
    >>> obj.valeur_externe
    '000'
    >>> obj.move_value('ERIC')
    >>> obj.valeur_externe
    'ERI'
    >>> obj = ZoneGroupe('zoneessai', 1, 0)
    >>> obj.nom
    'zoneessai'
    >>> objfilsimp = ZoneFilsSimple('essaifils', 5, picture = '999')
    >>> obj.ajout_fils_simple(objfilsimp)
    >>> objfilsimp2 = ZoneFilsSimple('essaifils2',5 , picture = '99')
    >>> obj.ajout_fils_simple(objfilsimp2)
    >>> obj.init_groupe()
    >>> obj.valeur_externe
    '00000'
    >>> obj.move_value('ERIC')
    >>> obj.valeur_externe
    'ERIC '
    >>> obj = ZoneGroupe('zoneessai', 1)
    >>> obj.nom
    'zoneessai'
    >>> objfilgrp = ZoneGroupe('essaifils', 2)
    >>> objfilsimp2 = ZoneFilsSimple('essaifils2',5 , picture = '99')
    >>> objfilgrp.ajout_fils_simple(objfilsimp2)
    >>> obj.ajout_fils_simple(objfilgrp)
    >>> objfilsimp3 = ZoneFilsSimple('essaifils5',5 , picture = 'XXXXX')
    >>> obj.ajout_fils_simple(objfilsimp3)
    #>>> obj.maj_longueur()
    #7
    #>>> obj.longueur_utile
    #7
    >>> obj.init_groupe()
    >>> obj.move_value('ERIC')
    >>> obj.valeur_externe
    'ERIC   '
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
    zone_groupe :ClassVar[list] = []

    def __post_init__(self):
        ZoneGroupe.zone_groupe.append(self)


    def ajout_fils_groupe(self, other):
        if other.rang <= self.rang :
            raise RuntimeError('Erreur sur le rang') 
        other.pere = self        
        self.longueur_utile += other.longueur_utile
        self.fils.append(other)

    def ajout_fils_simple(self, other):
        if other.rang <= self.rang :
            raise RuntimeError('Erreur sur le rang') 
        other.pere = self        
        self.longueur_utile += other.longueur_utile
        self.fils.append(other)

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
    
    def propage(self, valeur):
        for un_fils in self.fils : 
            if un_fils.son_type == 'GRP':
                valeur = un_fils.propage(valeur) 
            else:
                valeur_= valeur[:un_fils.longueur_utile]
                un_fils.valeur_externe = valeur_
                valeur = valeur[un_fils.longueur_utile:]
        return valeur        


@dataclass
class ZoneFilsSimple:
    ''' Cette classe permet de creer des zones simples qui iront sous de zones groupes
    >>> obj = ZoneFilsSimple('essaifils', 5, picture = '999')
    '''
    nom: str
    rang : int 
    section: str = 'NON RENSEIGNE'
    son_type: str = 'ALN'
    usage: str = 'DISPLAY'
    longueur_utile: int = 0  
    valeur_interne: str =''
    valeur_externe: str = ''
    picture: str =  '' 
    valeur_initialisation : str =  None     
    comportement_associe: object = None
    decimale : int = 0

    def __post_init__(self):
        self.initialize()

    def initialize(self):
        nature_ = Nature_pic(self.picture)
        self.son_type = nature_.nature
        self.longueur_utile =nature_.longueur
        if nature_.virgule:
            self.decimale = nature_.decimale
        comportement_ = Comportement(self.son_type , self.longueur_utile , self.valeur_initialisation )  
        comportement_.initialize()  
        #comportement_.initialize()
        self.valeur_externe = comportement_.valeur_externe
        self.valeur_interne = comportement_.valeur
        self.comportement_associe = comportement_
    
        
if __name__ == '__main__':  
    import doctest          
    doctest.run_docstring_examples(ZoneGroupe,None, verbose = 1)
    doctest.run_docstring_examples(ZoneFilsSimple,None, verbose = 1)
    
    