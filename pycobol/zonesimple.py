import re
from dataclasses import dataclass, field
from collections import defaultdict
from comportement  import *
from zonegroupe  import * 
from typing import ClassVar
from parser_cobol import *

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
    >>> a = ZoneGroupe.get_arbre()
    >>> print (len(a))
    2
    >>> arbre = ArbreZone()
    >>> len(arbre.redefine.keys()) 
    1
    >>> len(arbre.inv_redefine.keys()) 
    1
    '''
    def __init__(self, cible, *args, **kwargs):
        if type(cible)  == str:
            arbre = ArbreZone()
            cible = arbre.recherche_nom(cible)    
        self.cible = cible
        arbre.redefine[args[0]] = cible
        arbre.inv_redefine[cible.nom] = self
        super().__init__(*args, **kwargs)


class ZoneGroupeRedefine(ZoneGroupe):
    ''' Cette classe gère les clauses redefines de type zone groupe
    Le constructeur doit comporter la cible à redefinir
    >>> obj = ZoneFilsSimple('essaifils', 5, picture = '99999999')
    >>> obj2 = ZoneGroupeRedefine('essaifils', 'essairedefines' ,5) 
    >>> objj = ZoneFilsSimple('jj', 6, picture = '99')
    >>> objmm = ZoneFilsSimple('mm', 6, picture = '99')
    >>> objaa = ZoneFilsSimple('aaaa', 6, picture = '9999')
    >>> obj2.ajout_fils_simple(objj)
    >>> obj2.ajout_fils_simple(objmm)
    >>> obj2.ajout_fils_simple(objaa)
    >>> obj2.init_groupe()
    >>> a = ZoneGroupe.get_arbre()
    >>> print (len(a))
    5
    >>> arbre = ArbreZone()
    >>> len(arbre.redefine.keys()) 
    1
    >>> len(arbre.inv_redefine.keys()) 
    1
    '''
    def __init__(self, cible, *args, **kwargs):
        if type(cible)  == str:
            arbre = ArbreZone()
            cible = arbre.recherche_nom(cible)    
        self.cible = cible
        arbre.redefine[args[0]] = cible
        arbre.inv_redefine[cible.nom] = self
        super().__init__(*args, **kwargs)


if __name__ == '__main__':  
    import doctest          
    #doctest.run_docstring_examples(ZoneSimpleRedefine,None, verbose = 1)
    doctest.run_docstring_examples(ZoneGroupeRedefine,None, verbose = 1)