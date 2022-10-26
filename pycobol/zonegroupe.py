import re
from dataclasses import dataclass, field
from comportement  import *
from typing import ClassVar
from inspect import *
@dataclass
class ZoneGroupe:
    nom: str
    rang : int
    pere: int = 0
    fils : list =[]   
    son_type: str = 'GRP'
    usage: str = 'DISPLAY'
    longueur_utile: int = 0  
    valeur_interne: str =''
    valeur_externe: str = ''
    picture_resume: str =  '' 
    section: str = 'NON RENSEIGNE'
    
    def append_fils(self, fils):
        self.fils.append(fils)

    

if __name__ == '__main__':
    print("debut des tests internes")
    import doctest
    ZoneGroupe.affiche()
    ZoneGroupe.affiche_x()

