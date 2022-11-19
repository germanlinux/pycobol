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
print(principale.longueur_utile)
principale.move_value('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print('123456789012345678901234')
print(principale.valeur_externe,len(principale.valeur_externe) )
premier = zngrp.ZoneGroupe.recherche_nom('UNE')
print(premier.valeur_externe, len(premier.valeur_externe), 'UNE') 
deuxieme = zngrp.ZoneGroupe.recherche_nom('DEUXIEME')

print(deuxieme.valeur_externe, len(deuxieme.valeur_externe), 'deuxieme') 
nupsi = zngrp.ZoneGroupe.recherche_nom('DEUX1')
print(nupsi.valeur_externe, len(nupsi.valeur_externe)) 
cnaem = zngrp.ZoneGroupe.recherche_nom('DEUX2') 
print(cnaem.valeur_externe, len(cnaem.valeur_externe))  
trois = zngrp.ZoneGroupe.recherche_nom('TROISIEME') 
print('trois', trois.valeur_externe, len(trois.valeur_externe)) 
AAAA = zngrp.ZoneGroupe.recherche_nom('TROIS1') 
print(AAAA.valeur_externe, len(AAAA.valeur_externe)) 
print('______________________________')
print(cnaem.valeur_externe, len(cnaem.valeur_externe)) 
cnaem.move_to(AAAA)
print(AAAA.valeur_externe, len(AAAA.valeur_externe)) 
print(principale.valeur_externe)
for item in zngrp.ZoneGroupe.zone_groupe:
      print(item.nom, item.son_type)
