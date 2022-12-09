## essai de pycobol 
import sys
sys.path.insert(0, "../pycobol")
from pycobol import zonegroupe as zg
from pycobol import zonesimple as zs
zg2 ='''
                10            MADATE.                                   
                    11            AAAA   PICTURE  9(4).                 
                    11            MOIS   PICTURE  99.                      
                    11            JJ   PICTURE  99.                 
                10   DATEBRUT REDEFINE MADATE PIC 9(8).

        '''  
tlignes = zg.ZoneGroupe.fake_read_file_redefine()
len(tlignes)
arbre =zg.ZoneGroupe.read_groupe_from_code(tlignes)
len(arbre[0].fils)
print(zg.ZoneGroupe.vidage())
arbre.autonome(globals())
_madate.init_groupe()
_datebrut.move_value('20221209')
print(_madate.valeur_externe)
print(_aaaa.valeur_externe)
print(_mois.valeur_externe)
print(_jj.valeur_externe)

