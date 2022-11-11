## essai de pycobol 
import sys
print(sys.path)
sys.path.insert(0, "../pycobol")
from pycobol import zonegroupe as zngrp
zg5 = '''
10            PRINCIPALE.                              
      11            NUPSI  PICTURE  X(15). 
      11            DEUXIEME.
       12               CNAEM  PICTURE  9(5).               
       12            NUPEN  PICTURE  X(9).
      11            TROISIEME.
       12            AAAA  PIC XXX     
'''  

tlignes = zngrp.ZoneGroupe.fake_read_file(zg5)
zngrp.ZoneGroupe.read_groupe_from_code(tlignes) 
principale = zngrp.ZoneGroupe.zone_groupe[0]
principale.init_groupe()
print(principale.longueur_utile)
principale.move_value('CECI EST UN ESSAI DE MOVE DANS DES ZONES GROUPES')
print(len(principale.valeur_externe),principale.valeur_externe )

