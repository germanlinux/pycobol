## essai de pycobol 
import sys
sys.path.insert(0, "../pycobol")
from pycobol import zonegroupe as zg
from pycobol import zonesimple as zs

tlignes = zg.ZoneGroupe.fake_read_file_redefine()
len(tlignes)
zg.ZoneGroupe.read_groupe_from_code(tlignes)
arbre = zg.ZoneGroupe.get_arbre()
len(arbre[0].fils)
print(zg.ZoneGroupe.vidage())