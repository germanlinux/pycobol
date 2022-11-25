import re
from dataclasses import dataclass, field
from collections import defaultdict
from comportement  import *
from zonegroupe import *
from typing import ClassVar
from inspect import *
from zonage import *
from arbrezone import *
#################################
#   classe Zonefilssimple       #
#################################

@dataclass
class ZoneFilsSimple(ZoneGroupe):
    ''' Cette classe permet de creer des zones simples qui iront sous de zones groupes
    >>> obj = ZoneFilsSimple('essaifils', 5, picture = '999')
    '''
    
    picture: str =  '' 
    valeur_initialisation : str =  None     
    decimale : int = 0
    
    def __post_init__(self):
        self.initialize()
        
        arbre = ArbreZone()
        arbre.zone.append(self)
      
    def initialize(self):
        nature_ = Nature_pic(self.picture)
        self.son_type = nature_.nature
        self.longueur_utile =nature_.longueur
        if nature_.virgule:
            self.decimale = nature_.decimale
        comportement_ = Comportement(self.son_type , self.longueur_utile , self.valeur_initialisation )  
        comportement_.initialize()  
        self.valeur_externe = comportement_.valeur_externe
        self.valeur_interne = comportement_.valeur
        self.comportement_associe = comportement_
    

    

#################################
#   class  redefine       #
#################################

class ZoneSimpleRedefine(ZoneFilsSimple):
    ''' Cette classe gère les clauses redefines de type zone simple
    Le constructeur doit comporter la cible à redefinir
    >>> obj = ZoneFilsSimple('essaifils', 5, picture = '999')
    >>> obj2 = ZoneSimpleRedefine('essaifils', 'essairedefines' ,5, picture = 'XXX' )
    '''
    def __init__(self, cible, *args, **kwargs):
        if type(cible)  == str:
            arbre = ArbreZone()
            cible = arbre.recherche_nom(cible)    
        self.cible = cible
        super().__init__(*args, **kwargs)


if __name__ == '__main__':  
    import doctest          