from pycobol import zonage as zn


#er = zn.ZoneIndependante('essai','9(10)', None , None)
#print(er)
#print(zn.ZoneIndependante.zone_77)
ligne = "      77  MANUM PIC 9(10)."
obj = zn.ZoneIndependante.from_ligne(ligne)
print(obj.valeur_externe)
