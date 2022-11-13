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
       12               NUPEN  PICTURE  X(9).
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
deuxieme = zngrp.ZoneGroupe.recherche_nom('DEUXIEME')

print('deuxieme', deuxieme.valeur_externe, len(deuxieme.valeur_externe)) 
nupsi = zngrp.ZoneGroupe.recherche_nom('NUPSI')
print(nupsi.valeur_externe, len(nupsi.valeur_externe)) 
cnaem = zngrp.ZoneGroupe.recherche_nom('CNAEM') 
print(cnaem.valeur_externe, len(cnaem.valeur_externe)) 
nupen = zngrp.ZoneGroupe.recherche_nom('nupen') 
print(cnaem.valeur_externe, len(cnaem.valeur_externe)) 
trois = zngrp.ZoneGroupe.recherche_nom('TROISIEME') 
print('trois', trois.valeur_externe, len(trois.valeur_externe)) 
AAAA = zngrp.ZoneGroupe.recherche_nom('AAAA') 
print(AAAA.valeur_externe, len(AAAA.valeur_externe)) 
