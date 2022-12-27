import re
from dataclasses import dataclass, field
from comportement  import *
from parser_cobol import *
from typing import ClassVar
@dataclass
class Zone:
    ''' Classe de base des zones COBOL'''

    nom: str
    rang : int 
    section: str    
    son_type: str = 'ALN'
    usage: str = 'DISPLAY'
    longueur_utile: int = 0  
    valeur_interne: str =''
    valeur_externe: str = ''
    picture: str =  '' 
    valeur_initialisation : str =  ''     
    comportement_associe: object = None
    zone_77 :ClassVar[list] = []

    def __post_init__(self):
        self.initialize()

    def initialize(self):
        '''injection du comportement'''

        comportement_ = Comportement(self.son_type , self.longueur_utile , self.valeur_initialisation )  
       # print(comportement_)  
        comportement_.initialize()
        self.valeur_externe = comportement_.valeur_externe
        self.valeur_interne = comportement_.valeur
        self.comportement_associe = comportement_
     
    def move_value(self, newvalue ):
        ''' Cette methode permet d affecter des valeurs à une zone.
        Elle utilise les objets de la classe comportement.

        :param newvalue: nouvelle valeur

        '''
        self.comportement_associe.move_value(self,newvalue)

    
###############################
###############################
class Flottant(Zone):
    ''' Gère les zones a virgule flottante PIC ...V...'''

    def __init__(self,decimale,  nom , pic ,valeur_initiale = None , usage = 'DISPLAY'):
        self.decimale = decimale
        type_ = Nature_pic(pic).nature
        longueur_interne = Nature_pic(pic).longueur
        dec = Nature_pic(pic).decimale
        super().__init__(nom, 77, 'WS', type_ , usage, longueur_interne,None, None , pic, valeur_initiale)
        #print(self)
        Zone.zone_77.append(self)

    def initialize(self):
        comportement_ = ComportementFloat( self.decimale, self.son_type , self.longueur_utile , self.valeur_initialisation )  
        comportement_.initialize()
        self.valeur_externe = comportement_.valeur_externe
        self.valeur_interne = comportement_.valeur_interne 
        self.comportement_associe = comportement_      
      
    




class ZoneIndependante(Zone):
    ''' Zones qui sont en dehors des zones groupes'''

    def __init__(self, nom, pic, valeur = None ,usage= 'DISPLAY'  ): 
        type_ = Nature_pic(pic).nature
        longueur_interne = Nature_pic(pic).longueur
        dec = Nature_pic(pic).decimale
        super().__init__(nom, 77, 'WS', type_ , usage, longueur_interne,None, None , pic, valeur )
        Zone.zone_77.append(self)
    @classmethod
    def liste_ws(cls):
        return ZoneIndependante.zone_77


    @classmethod
    def  from_ligne(cls, ligne):
        ''' Prise en charge des zones elementaires de niveau 77
        a partir d'une ligne COBOL
        
        :param  str ligne:  la ligne cobol a analyser
        
        >>> ligne = '      77  MAZONE PIC X(10).'
        >>> obj =ZoneIndependante.from_ligne(ligne)
        >>> obj.son_type
        'ALN'
        >>> obj.longueur_utile
        10
        >>> obj.picture
        'X(10)'
        
        >>> ligne = "      77  MAZONE PIC X(10) VALUE 'er'."
        >>> obj =ZoneIndependante.from_ligne(ligne)
        >>> obj.son_type
        'ALN'
        >>> obj.longueur_utile
        10
        >>> obj.picture
        'X(10)'
        >>> obj.valeur_initialisation
        'er'
        >>> obj.valeur_interne
        'er'
        
        >>> ligne = "      77  MAZONE PIC 999."
        >>> obj =ZoneIndependante.from_ligne(ligne)
        >>> obj.son_type
        'NUM'
        >>> obj.longueur_utile
        3
        
        >>> obj.picture
        '999'
        >>> obj=ZoneIndependante.from_ligne("77  NPAG PIC 9999 VALUE 0.")
        >>> obj.valeur_interne
        0
        
        >>> obj=ZoneIndependante.from_ligne("77  NPAG PIC 9999 VALUE ZERO.")
        >>> obj.valeur_interne
        0
        >>> obj=ZoneIndependante.from_ligne("77  NPAG PIC S999V99 VALUE ZERO.")
        >>> obj.valeur_interne
        0
        >>> obj.son_type
        'SFLOAT'
        >>> obj.longueur_utile
        5
        >>> obj=ZoneIndependante.from_ligne("77  NPAG PIC S999 VALUE ZERO.")
        >>> obj.valeur_interne
        0
        >>> obj=ZoneIndependante.from_ligne("77  NPAG PIC S9(3) VALUE ZERO.")
        >>> obj.valeur_interne
        0
        >>> obj=ZoneIndependante.from_ligne("77  NPAG PIC 9(3)V99 VALUE ZERO.")
        >>> obj.valeur_interne
        0.0
        >>> obj.son_type
        'FLOAT'
        >>> obj.longueur_utile
        5
         >>> ligne = "      77  MAZONE PIC X(10) VALUE SPACE."
        >>> obj =ZoneIndependante.from_ligne(ligne)
        >>> obj.son_type
        'ALN'
        >>> obj.longueur_utile
        10
        >>> obj.valeur_interne
        ''
        >>> ligne = "      77  MAZONE PIC X(10)."
        >>> obj =ZoneIndependante.from_ligne(ligne)
        >>> obj.valeur_externe
        '          '
        >>> ligne = "      77  MANUM PIC 9(10)."
        >>> obj =ZoneIndependante.from_ligne(ligne)
        >>> obj.valeur_externe
        '0000000000'

    '''
        if ligne[-1] == '\n':
            ligne= ligne[:-1]
        
        ligne_origine = ligne
        ligne = ligne.strip()
        result = re.sub(' +', ' ', ligne)
        tab = result.split(' ')
        if tab[-1][-1] == '.' :
            tab[-1] = tab[-1][:-1]    
        if tab[0] != '77':
            return None
        (type_,pic, longueur,decimale) =  Zone.traite_pic(tab)
        #longueur_interne  = longueur
        valeur_externe = None
        valeur = Zone.traite_value(tab)
        usage = Zone.traite_usage(tab)
        if decimale:        
            return Flottant(decimale, tab[1] ,  pic, valeur, usage )
        else:
            return cls(tab[1] ,  pic, valeur, usage)
    
    def move_from(self, emetteur):
        pass    

    def init_variable(self):
        if not self.valeur:
            pass
            



if __name__ == '__main__':
    print("debut des tests internes")
    import doctest
    doctest.run_docstring_examples(ZoneIndependante.from_ligne,None, verbose = False)
    doctest.run_docstring_examples(Nature_pic,None, verbose = False)
    doctest.run_docstring_examples(Zone.traite_value,None, verbose = False)
    doctest.run_docstring_examples(Zone.extract_niveau, None, verbose = False)
    print("fin des tests internes")