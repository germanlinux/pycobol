## essai de pycobol 
import sys
sys.path.insert(0, "../pycobol")
from pycobol import zonegroupe as zngrp
zg5 = '''
10            PRINCIPALE.                              
      11            UNE  PICTURE  X(5). 
      11            DEUXIEME.
       12               DEUX1  PICTURE  9(5).               
       12               DEUX2  PICTURE  X(9).
      11            TROISIEME.
       12            TROIS1  PIC XXX     
'''  

tlignes = zngrp.ZoneGroupe.fake_read_file(zg5)
zngrp.ZoneGroupe.read_groupe_from_code(tlignes) 
principale = zngrp.ZoneGroupe.zone_groupe[0]
principale.init_groupe()
zngrp.ZoneGroupe.autonomme(globals())


print(principale.longueur_utile)
principale.move_value('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print('123456789012345678901234')
print(principale.valeur_externe,len(principale.valeur_externe) )

print(_UNE.valeur_externe, len(_UNE.valeur_externe), 'UNE') 
print(_DEUXIEME.valeur_externe, len(_DEUXIEME.valeur_externe), 'deuxieme') 
print(_DEUX1.valeur_externe, len(_DEUX1.valeur_externe)) 

print(_DEUX2.valeur_externe, len(_DEUX2.valeur_externe))  
trois = zngrp.ZoneGroupe.recherche_nom('TROISIEME') 
print('trois', _TROISIEME.valeur_externe, len(_TROISIEME.valeur_externe)) 

print("debut")
#for cle in zngrp.ZoneGroupe.arbreInverse:
#      print(cle,zngrp.ZoneGroupe.arbreInverse[cle] )

#cnaem.move_to(AAAA)
#print(AAAA.valeur_externe, len(AAAA.valeur_externe)) 
#print(principale.valeur_externe)
for item in zngrp.ZoneGroupe.zone_groupe:
      print(item.nom)
      if item.nom == 'DEUX2':
            print(item.picture)