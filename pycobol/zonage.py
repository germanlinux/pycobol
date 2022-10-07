import re
from dataclasses import dataclass, field

@dataclass
class Zone:
    nom: str
    rang : int 
    section: str    
    son_type: str = 'ALN'
    usage: str = 'DISPLAY'
    pere: int = 0
    prec: int = 0
    suivant : int = 0    
    longueur_interne: int = 0  
    longueur_externe: int = 0
    picture: str =  '' 
    value : str =  ''   
    nature_value : str = ''    
        
    @staticmethod
    def traite_pic(t_ligne):
         debpic = -1
         finpic = -1
         for cp, val in  enumerate(t_ligne) :
                if val == 'PIC' or val == 'PICTURE':
                    debpic = cp + 1
                    break
         for cp, val in  enumerate(t_ligne[debpic:], start = debpic) :
                if val == 'VALUE' :
                    finpic = cp - 1
                    break    
         else:
            finpic = len(t_ligne) - 1
         pic = ' '.join(t_ligne[debpic:finpic +1])
         nature_ = Nature_pic(pic)
         nature = nature_.nature
         nature_obj = nature_
         long = nature_obj.longueur                  
         return nature, pic, long
        

    def traite_value(t_ligne):
        ''' Traitement des values dans la working storage
            :param str tableau mot de la ligne
            >>> ligne =   ['77', 'MAZONE', 'PIC', 'X(10)', 'VALUE', 'SPACE']
            >>> Zone.traite_value(ligne)
            ('', 'STR')
            >>> ligne =   ['77', 'MAZONE', 'PIC', 'X(10)', 'VALUE', "'er'"]
            >>> Zone.traite_value(ligne)
            ('er', 'STR')
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
            return None, None         
        value_ = value.translate(str.maketrans({"\'":'' ,'\"':'' }))
        if value_ != value:
            nature_value = 'STR'
        else:    
            try: 
                #print('try', value_)
                (value_ , nature_value) = dico_[value_] 
            except: 
                value_ = int(value)
                nature_value  = 'NUM'
            
        return value_,nature_value

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
        self.longueur = long
 




class ZoneIndependante(Zone):
    
    def __init__(self, nom,type_,  longueur_int, longueur_externe  , pic, valeur, nature_valeur ): 
        super().__init__(nom, 77, 'WS', type_ , 'DISPLAY',0, 0, 0, longueur_int, longueur_externe, pic, valeur ,nature_valeur )
       # print(self)
    @classmethod
    def  from_ligne(cls, ligne):
        ''' Prise en charge des zones elementaires de niveau 77
        a partir d'une ligne COBOL
        
        :param  str ligne:  la ligne cobol a analyser
        
        >>> ligne = '      77  MAZONE PIC X(10).'
        >>> obj =ZoneIndependante.from_ligne(ligne)
        >>> obj.son_type
        'ALN'
        >>> obj.longueur_interne
        10
        >>> obj.picture
        'X(10)'
        
        >>> ligne = "      77  MAZONE PIC X(10) VALUE 'er'."
        >>> obj =ZoneIndependante.from_ligne(ligne)
        >>> obj.son_type
        'ALN'
        >>> obj.longueur_interne
        10
        >>> obj.picture
        'X(10)'
        >>> obj.value
        'er'
        >>> ligne = "      77  MAZONE PIC 999."
        >>> obj =ZoneIndependante.from_ligne(ligne)
        >>> obj.son_type
        'NUM'
        >>> obj.longueur_interne
        3
        
        >>> obj.picture
        '999'
        >>> obj=ZoneIndependante.from_ligne("77  NPAG PIC 9999 VALUE 0.")
        >>> obj.value
        0
        >>> obj.nature_value
        'NUM'
        
        >>> obj=ZoneIndependante.from_ligne("77  NPAG PIC 9999 VALUE ZERO.")
        >>> obj.value
        0
        >>> obj=ZoneIndependante.from_ligne("77  NPAG PIC S999V99 VALUE ZERO.")
        >>> obj.value
        0
        >>> obj.son_type
        'SFLOAT'
        >>> obj.longueur_interne
        5
        >>> obj=ZoneIndependante.from_ligne("77  NPAG PIC S999 VALUE ZERO.")
        >>> obj.value
        0
        >>> obj=ZoneIndependante.from_ligne("77  NPAG PIC S9(3) VALUE ZERO.")
        >>> obj.value
        0
        >>> obj=ZoneIndependante.from_ligne("77  NPAG PIC 9(3)V99 VALUE ZERO.")
        >>> obj.value
        0
        >>> obj.son_type
        'FLOAT'
        >>> obj.longueur_interne
        5
        >>> obj.nature_value
        'NUM'
         >>> ligne = "      77  MAZONE PIC X(10) VALUE SPACE."
        >>> obj =ZoneIndependante.from_ligne(ligne)
        >>> obj.son_type
        'ALN'
        >>> obj.longueur_interne
        10
        >>> obj.value
        ''
        
    '''
        # enlever blanc en tete et fin
        # remplace blancs par 1 blanc
        # splitter la ligne
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
        (type_,pic, longueur) =  Zone.traite_pic(tab)
        longueur_interne  = longueur_externe = longueur
        (valeur, nature) = Zone.traite_value(tab) 
        
        return cls(tab[1] ,type_, longueur_interne,  longueur_interne, pic, valeur , nature)


if __name__ == '__main__':
    print("debut des tests internes")
    import doctest
    doctest.run_docstring_examples(ZoneIndependante.from_ligne,None, verbose = False)
    doctest.run_docstring_examples(Nature_pic,None, verbose = False)
    doctest.run_docstring_examples(Zone.traite_value,None, verbose = False)
    print("fin des tests internes")