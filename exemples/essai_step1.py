## essai de pycobol 
import sys
sys.path.insert(0, "../pycobol")
from pycobol import zonage as zn

obj2 = zn.ZoneIndependante( 'MAZONE1', '9(5)')
obj3 = zn.ZoneIndependante( 'MAZONE2', 'X(5)')
obj2.move_value(12)
print(obj2.valeur_externe)
obj2.move_value('12')
print(obj2.valeur_externe)
obj3.move_value(12)
print(obj3.valeur_externe)
obj3.move_value('12')
print(obj3.valeur_externe)


