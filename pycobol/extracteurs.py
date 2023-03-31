import re
def extract_type_data(objet):
    if type(objet) == str :
                    return 'ALP'
    elif type(objet) == int:
                    return 'NUM'
    elif type(objet) == float
                    return 'NUM'    
    else:
        return 'DATA'
                    
def extract_niveau(t_ligne):
        ''' retourne le niveau cobol de la ligne

        :param t_ligne: liste de ligne
        :type t_ligne: list

        >>> extract_niveau(['10'] ,'WW04-DAEC'.])
        10
        >>> extract_niveau(['11'] ,'WW04-DAEC'.])
        11
        '''
        tniv = re.search(r'(\d+)', t_ligne[0])
        if  tniv :
            return int(tniv[1])
        else:
            return 0
  
def extract_nom(t_ligne):
        ''' retourne le nom de la zone

        :param t_ligne: liste de ligne
        :type t_ligne: list

        >>> extract_niveau(['10'] ,'WW04-DAEC.'])
        'WW04-DAEC'
        >>> extract_niveau(['11'] ,'WW04-DAEC'])
        'WW04-DAEC'
        '''
        tniv = re.search('(.+).?', t_ligne[1])
        if  tniv:
            return tniv[1]
        else:
            return None

def traite_pic(t_ligne):
         ''' return Nature.nature, pic, Nature.longueur , Nature.decimale

         :param t_ligne: liste de ligne
         :type t_ligne: list
         '''

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




def traite_redefine(liste):
        for cp, val in  enumerate(liste) :
                if val == 'REDEFINE':
                    nom = liste[cp-1]
                    cible= liste[cp+1]
                    del (liste[cp])
                    del (liste[cp])
                    break

        return cible, liste   

def traite_usage(t_ligne):
    usage = 'DISPLAY'
    for cp, val in  enumerate(t_ligne) :
        if val == 'COMP' :
             usage = 'COMP'
             break

    return usage                   

def traite_value(t_ligne):
    ''' Traitement des values dans la working storage

    :param t_ligne: liste de ligne
    :type t_ligne: list

    >>> ligne =   ['77', 'MAZONE', 'PIC', 'X(10)', 'VALUE', 'SPACE']
    >>> Zone.traite_value(ligne)
    ''
    >>> ligne =   ['77', 'MAZONE', 'PIC', 'X(10)', 'VALUE', "'er'"]
    >>> traite_value(ligne)
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

    
##############################
###   class  Nature_pic   ####
##############################

class Nature_pic():
    ''' Traitement du format d'une clause PIC 
        
    :param pic: format pic à traiter
    :type pic: str

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
 

if __name__ == '__main__':   # pragma: no cover
    import doctest          
    doctest.run_docstring_examples(traite_filler,None, verbose = 1)
    doctest.testmod()