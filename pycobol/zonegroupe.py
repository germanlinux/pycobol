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
    
    def ajout_fils_groupe(self, other):
        if other.rang <= self.rang :
            raise RuntimeError('Erreur sur le rang') 
        other.pere = self        
        self.longueur_utile += other.longueur_utile
        self.fils.append(other)

if __name__ == '__main__':  
    import doctest          
    doctest.run_docstring_examples(ZoneGroupe,None, verbose = 1)
    