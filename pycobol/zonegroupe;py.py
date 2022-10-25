import re
from dataclasses import dataclass, field
from comportement  import *
from typing import ClassVar
@dataclass
class ZoneGroupe:
    nom: str
    rang : int
    pere: int 
    frere:: int
    fils : list    
    son_type: str = 'GRP'
    usage: str = 'DISPLAY'
    longueur_utile: int = 0  
    valeur_interne: str =''
    valeur_externe: str = ''
    picture_resume: str =  '' 
    section: str = 'NON RENSEIGNER'
    