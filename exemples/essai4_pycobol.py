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
redef = zngrp.ZoneSimpleRedefine('TROIS1', 'essairedefines' ,12, picture = '999' )
print(redef.cible)