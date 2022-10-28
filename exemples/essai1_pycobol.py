## essai de pycobol 
import sys
print(sys.path)
sys.path.insert(0, "../pycobol")
from pycobol import zonage as zn
ligne = "      77  MANUM PIC 9(6)."
obj = zn.ZoneIndependante.from_ligne(ligne)
print(obj.valeur_externe)
obj2 = zn.ZoneIndependante( 'MAZONE1', '9(3)', 200)
print((obj2.valeur_externe))
obj3= zn.Flottant( 2, 'MAZONE1V', '9(3)V99', 200)
print((obj3.valeur_externe))
obj4 = zn.ZoneIndependante( 'MAZONE2', 'S9(3)', 200)
print((obj4.valeur_externe))
obj5= zn.Flottant( 2, 'MAZONE2V', 'S9(3)V99', -200)
print((obj5.valeur_externe))
for item in zn.Zone.zone_77:
    print(item.nom , item.son_type, item.valeur_externe, item.valeur_interne)

'''
000000
200
200,00
+200
-200,00
MANUM NUM 000000 0
MAZONE1 NUM 200 200
MAZONE1V FLOAT 200,00 200.0
MAZONE2 SNUM +200 200
MAZONE2V SFLOAT -200,00 -200.0
'''
