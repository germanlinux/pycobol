import re
from dataclasses import dataclass, field
from comportement  import *
from typing import ClassVar
from inspect import *
@dataclass
class ZoneGroupe:
    ''' Cette classe prend en charge la creation d'une zone groupe 
    par nature cette zone est de type ALN.
    Sa longueur est la somme des longueurs des composants qui la composent
    >>> obj = ZoneGroupe('zoneessai', 1, 0)
    >>> obj.nom
    'zoneessai'
    >>> print(obj)
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
    picture_resume: str =  '' 
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

@dataclass
class ZoneFilsSimple:
    ''' Cette classe permet de creer des zones simples qui iront sous de zones groupes
    >>> obj = ZoneFilsSimple('essaifils', 5, picture = '999')
    >>> print(obj) 

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
    valeur_initialisation : str =  ''     
    comportement_associe: object = None

    def __post_init__(self):
        self.initialize()

    def initialize(self):
       
        comportement_ = Comportement(self.son_type , self.longueur_utile , self.valeur_initialisation )  
       # print(comportement_)  
        comportement_.initialize()
        self.valeur_externe = comportement_.valeur_externe
        self.valeur_interne = comportement_.valeur
        self.comportement_associe = comportement_
    
if __name__ == '__main__':  
    import doctest          
    doctest.run_docstring_examples(ZoneGroupe,None, verbose = 1)
    doctest.run_docstring_examples(ZoneFilsSimple,None, verbose = 1)
    
    