import re
from dataclasses import dataclass, field
from comportement  import *

@dataclass
class Zone:
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


    def __post_init__(self):
        self.initialize()

    def initialize(self):
       
        comportement_ = Comportement(self.son_type , self.longueur_utile , self.valeur_initialisation )  
       # print(comportement_)  
        comportement_.initialize()
        self.valeur_externe = comportement_.valeur_externe
        self.valeur_interne = comportement_.valeur
        self.comportement_associe = comportement_
     
    def move_value(self, newvalue ):
        ''' Cette methode permet d affecter des valeurs à une zone.
        Elle utilise les objets de la classe comportement.
        '''
        self.comportement_associe.move_value(self,newvalue)



    @staticmethod
    def traite_pic(t_ligne):
         ''' return nature_.nature, pic, nature_.longueur , nature_.decimale'''
         debpic = -1
         finpic = -1
         for cp, val in  enumerate(t_ligne) :
                if val == 'PIC' or val == 'PICTURE':
                    debpic = cp + 1
                    break
         for cp, val in  enumerate(t_ligne[debpic:], start = debpic) :
                if val == 'VALUE' or val =='COMP' :
                    finpic = cp - 1
                    break    
         else:
            finpic = len(t_ligne) - 1


         pic = ' '.join(t_ligne[debpic:finpic +1])
         nature_ = Nature_pic(pic)             
         return nature_.nature, pic, nature_.longueur , nature_.decimale
    
    @staticmethod
    def traite_usage(t_ligne):
        usage = 'DISPLAY'
        for cp, val in  enumerate(t_ligne) :
            if val == 'COMP' :
                 usage = 'COMP'
                 break

        return usage                   

    @staticmethod
    def traite_value(t_ligne):
        ''' Traitement des values dans la working storage
            :param str tableau mot de la ligne
            >>> ligne =   ['77', 'MAZONE', 'PIC', 'X(10)', 'VALUE', 'SPACE']
            >>> Zone.traite_value(ligne)
            ''
            >>> ligne =   ['77', 'MAZONE', 'PIC', 'X(10)', 'VALUE', "'er'"]
            >>> Zone.traite_value(ligne)
            'er'
        '''    

        debval = -1
        finval = -1
        dico_ = {'ZERO'  : (0, 'NUM'), 
                  'ZEROS' : (0, 'NUM'),
                  'SPACE' : ('', 'STR'),
                  'SPACES': ('', 'STR'),
        }
        value = ''
        for cp, val in  enumerate(t_ligne) :
            if val == 'VALUE' :
                 nature_value = 'STR'
                 value = ' '.join(t_ligne[debval:])
                 break
        else: 
            return None        
        value_ = value.translate(str.maketrans({"\'":'' ,'\"':'' }))
        if value_ == value:
            try: 
                #print('try', value_)
                (value_ , nature_value) = dico_[value_] 
            except: 
                if ','  in value:
                    value = value.replace(',','.')
                    value_ = float(value)
                else:
                    value_ = int(value)
            
        return value_

###############################
###############################
class Flottant(Zone):
    def __init__(self,decimale,  nom , pic ,valeur_initiale = None , usage = 'DISPLAY'):
        self.decimale = decimale
        type_ = Nature_pic(pic).nature
        longueur_interne = Nature_pic(pic).longueur
        dec = Nature_pic(pic).decimale
        super().__init__(nom, 77, 'WS', type_ , usage, longueur_interne,None, None , pic, valeur_initiale)
        #print(self)

    def initialize(self):
        comportement_ = ComportementFloat( self.decimale, self.son_type , self.longueur_utile , self.valeur_initialisation )  
        comportement_.initialize()
        self.valeur_externe = comportement_.valeur_externe
        self.valeur_interne = comportement_.valeur_interne 
        self.comportement_associe = comportement_      
      
    

class Nature_pic():
    ''' Traitement du format d'une clause PIC 
        :param str  pic : format pic à traiter
        >>> obj = Nature_pic('999')
        >>> obj.nature
        'NUM'
        >>> obj.longueur
        3
        >>> obj = Nature_pic('S999')
        >>> obj.nature
        'SNUM'
        >>> obj.longueur
        3
        >>> obj.virgule
        False
        >>> obj = Nature_pic('99V9')
        >>> obj.nature
        'FLOAT'
        >>> obj.longueur
        3
        >>> obj.longueur
        3
        >>> obj = Nature_pic('S99V9')
        >>> obj.nature
        'SFLOAT'
        >>> obj.longueur
        3
        >>> obj.virgule
        True
        >>> obj = Nature_pic('XX')
        >>> obj.nature
        'ALN'
        >>> obj.longueur
        2

    '''
    support = {'X' :'ALN' , '9' :'NUM', 'S' :'SNUM' ,'A' :'ALP'}

    def __init__(self, pic):
        self.pic = pic
        self.nature = self.support.get(self.pic[0])
        self.decimale = 0
        if not self.nature :
            raise Exception(f"FORMAT Picture NON SUPPORTE: {pic}")
        else:
            self.pose_virgule()
            self.calcul_longueur()

    def pose_virgule(self):
        if self.nature[-3:] == 'NUM' and 'V' in self.pic :
            self.virgule = True
            self.nature = self.nature.replace('NUM', 'FLOAT')
        else:
            self.virgule = False

    def calcul_longueur(self):
        tabv = re.findall(r'\(\d+\)', self.pic)
        long = -1
        flag_par = 0
        if tabv:
            for i, item in enumerate(tabv):
                item = item.translate(str.maketrans({'(':'' ,')':'' }))
                tabv[i]  = item
                flag_par = 1
            long = int(tabv[0])    
        else :
            long = len(self.pic)
        if self.pic[0] == 'S' and flag_par == 0:
            long -= 1
        if self.virgule : 
            if flag_par == 0 :
                long -= 1
            else:    
                tab_ = re.search(r'V(9+)' ,self.pic)
                if tab_:
                    long += len(tab_[1])
                    self.decimale = len(tab_[1])
        self.longueur = long
 




class ZoneIndependante(Zone):
    zone_77 = []

    def __init__(self, nom, pic, valeur = None ,usage= 'DISPLAY'  ): 
        type_ = Nature_pic(pic).nature
        longueur_interne = Nature_pic(pic).longueur
        dec = Nature_pic(pic).decimale
        super().__init__(nom, 77, 'WS', type_ , usage, longueur_interne,None, None , pic, valeur )
        ZoneIndependante.zone_77.append(self)
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
    print("fin des tests internes")