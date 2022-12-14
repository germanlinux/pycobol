import re
from arbrezone import *
from zonegroupe import * 
from extracteurs import *
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
        return(lignes)

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
          



if __name__ == '__main__':  
    import doctest          
    #    print("debut des tests internes")
    doctest.run_docstring_examples(traite_filler,None, verbose = 1)
    doctest.testmod()
    print("fin des tests internes")

    