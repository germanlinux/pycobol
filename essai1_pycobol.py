## essai de pycobol 
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


