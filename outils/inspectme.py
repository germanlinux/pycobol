import sys
sys.path.insert(0, "../pycobol")
from pycobol import zonegroupe as zngp
from pycobol import comportement as cp
from pycobol import zonage as zn 
from inspect import getmembers, signature
listem = getmembers(zn.Zone)
for item in listem:
    if '__' not in item[0]:
        if 'func' in str(item[1]):
            print(item[0], ':methode')
        else:
            print(item[0], ':Attribut')    
print(signature(zn.Zone))