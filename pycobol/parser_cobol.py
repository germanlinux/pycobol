import re
from arbrezone import ArbreZone
from zonegroupe import ZoneGroupe
from extracteurs import extract_nom, extract_niveau, traite_pic, traite_redefine
from execution import Program, Etiquette, Instruction
def fake_read_file(data= None):
    zg1 ='''
            10            MADATE.                                   
                11            AAAA   PICTURE  9(4).                 
                11            MOIS   PICTURE  99.                      
                11            JJ   PICTURE  99.                 
    '''            
    zg2 ='''
            10            MADATE.                                   
                11            AAAA   PICTURE  9(4).                 
                11            MOIS   PICTURE  99.                      
                11            JJ   PICTURE  99.                 
            10   DATEBRUT REDEFINE MADATE PIC 9(8).'''            
    
    if not data:
      data = zg1
    if data == 'REDEFINE' :
        data = zg2
    t_zg1 = data.split('\n')
    lignes = [item  for item in t_zg1 if item]
    return (lignes)

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
    import redefine
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

def decode_move(reg)
    ...
    

def recherche_instruction(ligne):
    t_stop = re.match('STOP RUN', ligne)
    if t_stop:
        _inst = Instruction('stop_run')
        return _inst
    t_display = re.match('DISPLAY ', ligne)
    if t_display:
        suite = ligne[t_display.span()[1]:]
        if suite[-1] == '.' :
            suite =  suite[:-1]
        # on fait une boucle pour rechercher les mots 
        # il faudra une autre boucle pour trouver les donnees
        argl = []
        while  len(suite) >  1:
            suite = suite.lstrip() 
            re_guil = re.match(r'(?P<quote>\")(.+)(?P=quote)', suite)
            if re_guil: # c est une chaine de caractere
                argl.append(re_guil[2])
                suite= suite[re_guil.span(2)[1] + 1:]    
            else: # c est un nom de donnée
                re_data= re.match(r'([a-zA-Z0-9]+)', suite)
                if re_data:
                    arbre = ArbreZone()
                    _data= arbre.recherche_nom(re_data[1])
                    argl.append(_data)
                    suite= suite[re_data.span()[1]:]   
        _inst = Instruction('display',argl)
        return _inst    
    t_accept = re.match('ACCEPT ', ligne)
    if t_accept:
        f_date = 0
        suite = ligne[t_accept.span()[1]:]
        if suite[-1] == '.' :
            suite =  suite[:-1]
        t_from = re.search(r'FROM\s+DATE', suite)
        if t_from:
            f_date = 1
        t_data_ = re.search(r'([^ ]+)',suite )
        if t_data_:
           arbre = ArbreZone()
           _data= arbre.recherche_nom(t_data_[1])
                    
        if f_date:
            _inst= Instruction('accept',[_data , 'DATE'])
        else:
            _inst= Instruction('accept',[_data])
            
        return _inst        
     t_move = re.match('MOVE ', ligne)   
     if t_move:
        _inst = decode_move(t_move)
        return _inst

def load_procedure(tcode):
    ''' Cette fonction transforme une liste de ligne cobol en modele Python

    :param liste: programme COBOL a charger
    :type liste: list  

    >>> tligne = fake_read_file_proc()
    >>> pgm = load_procedure(tligne)
    >>> print(pgm.vidage()) # doctest: +ELLIPSIS
    E...
    <BLANKLINE>

    '''
    for ligne in tcode:
       if ligne[-1] == '\n':
           ligne= ligne[:-1]

       if 'PROCEDURE DIVISION' in ligne:
          lignew = ligne.lstrip()
          debut = len(ligne) - len(lignew)
          pgm = Program('demo')
       else:
           lignew = ligne.lstrip()
           if debut == len(lignew):  # c est une etiquette
               esent = ligne.strip()
               if esent[-1] == '.' :
                   esent = esent[:-1]
               _etq = Etiquette(esent)
               pgm.add_etiquette(_etq) 
           else:  # une instruction
               _inst  = recherche_instruction(lignew)
               pgm.add_step(_inst)
    return pgm

def fake_read_file_proc(data= None):
    ''' Cette fonction emule le chargement d'une série de ligne issues de la lecture
    d'un fichier contenant une procedure cobol'''

    zg1 ='''        PROCEDURE DIVISION.
                             DISPLAY "Hello world".
                             STOP RUN.'''
    if not data:
        data = zg1
    t_zg1 = data.split('\n')
    lignes = [item  for item in t_zg1 if item and item[0] != '*']
    return (lignes)                               


if __name__ == '__main__':  
    import doctest          
    #    print("debut des tests internes")
    doctest.run_docstring_examples(load_procedure,None, verbose = 1)
    #doctest.testmod()
    print("fin des tests internes")

    