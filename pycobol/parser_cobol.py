import re
from arbrezone import *
from zonegroupe import * 
def extract_niveau(t_ligne):
        ''' retourne le niveau cobol de la ligne

        :param t_ligne: liste de ligne
        :type t_ligne: list

        >>>extract_niveau(['10'] ,'WW04-DAEC'.])
        10
        >>>extract_niveau(['11'] ,'WW04-DAEC'.])
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



def read_groupe_from_code(tcode):
        ''' cette fonction prend comme parametre en entrée un tableau de ligne
        et en fonction du contenu active un constructeur de groupe ou de zone simple et traite les redefines
        
        >>> tlignes = ZoneGroupe.fake_read_file()
        >>> len(tlignes)
        4
        >>> ZoneGroupe.read_groupe_from_code(tlignes)
        >>> arbre = (ZoneGroupe.get_arbre())
        >>> len(arbre[0].fils)
        3
        Pour un redefine :
        >> tlignes = ZoneGroupe.fake_read_file_redefine()
        >>> print(tlignes)   
        >>> len(tlignes)
        5
        >>> ZoneGroupe.read_groupe_from_code(tlignes)
        >>> arbre = ZoneGroupe.get_arbre()
        >>> len(arbre[0].fils)
        3
        >>> ZoneGroupe.vidage()
        '''
        import zonesimple
        import redefine
        _zonegrp_active = ''
        _niveaux_max = 99
        ### to do : mutualiser
        for ligne in tcode:
            if ligne[-1] == '\n':
                ligne= ligne[:-1]
        
            ligne = ligne.strip()
            result = re.sub(' +', ' ', ligne)
            if result:
                tab = result.split(' ')
                if tab[-1][-1] == '.' :
                    tab[-1] = tab[-1][:-1]
            else:
                break
            niv = extract_niveau(tab)
            _nom = extract_nom(tab)
            flagredef = 0
            if 'REDEFINE'  in ligne:
                cible,tab = traite_redefine(tab)
                flagredef = 1
            arbre = ArbreZone()
            obt = arbre.recherche_rang(niv)    

            if ' PIC '  in ligne  or ' PICTURE ' in ligne:
                arbre = ArbreZone()
                if len(arbre.zone) == 0:
                    niveaux_max = 0
                else: 
                    niveaux_max = arbre.zone[-1].rang
                ##  traiter le redefine ##
                (type_,pic, longueur,decimale) =  traite_pic(tab)
                
                if flagredef:
                   obj_s = redefine.ZoneSimpleRedefine(cible, _nom,niv ,picture = pic)
                   
                else:    
                    obj_s = redefine.ZoneFilsSimple(_nom,niv ,picture = pic )
                    if obt :
                        obt.ajout_fils_simple(obj_s) 
            else:    
                if flagredef:
                       obj_p = redefine.ZoneGroupeRedefine(cible, _nom,niv) 
                else:   
                       obj_p = ZoneGroupe(_nom, niv)
                       if obt :
                            obt.ajout_fils_simple(obj_p)
                    
        return arbre            
                ## est ce le niveau le plus haut ?
                ##  ca peut etre une zone groupe dans une zone groupe  
          



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
 



    