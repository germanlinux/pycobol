## essai de pycobol 
import sys
sys.path.insert(0, "../pycobol")
from pycobol import zonegroupe as zngrp
from pycobol import zonesimple as zngrps
from pycobol import arbrezone as arbre


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
monarbre = zngrp.ZoneGroupe.read_groupe_from_code(tlignes) 
print(len(monarbre.zone))
print(len(zngrp.ZoneGroupe.get_arbre()))

monarbre.autonomme(globals())
_principale.init_groupe()
print(_principale.longueur_utile)
_principale.move_value('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print('123456789012345678901234')
print(_principale.valeur_externe,len(_principale.valeur_externe) )
print(_une.valeur_externe, len(_une.valeur_externe), 'UNE') 
print(_deuxieme.valeur_externe, len(_deuxieme.valeur_externe), 'deuxieme') 
print(_deux1.valeur_externe, len(_deux1.valeur_externe)) 
print(_deux2.valeur_externe, len(_deux2.valeur_externe))  
print('trois', _troisieme.valeur_externe, len(_troisieme.valeur_externe)) 

print("debut")
#for cle in zngrp.ZoneGroupe.arbreInverse:
#      print(cle,zngrp.ZoneGroupe.arbreInverse[cle] )

#cnaem.move_to(AAAA)
#print(AAAA.valeur_externe, len(AAAA.valeur_externe)) 
#print(principale.valeur_externe)
for item in monarbre.zone:
      print(item.nom)
      if item.nom == 'DEUX2':
            print(item.picture)

monarbre.retroArbre()
for item, value in monarbre.inverse.items():
      print(item , value )
