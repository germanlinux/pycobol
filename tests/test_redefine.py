import sys
sys.path.insert(0, "../pycobol")
from pycobol import zonage as zn
from pycobol import zonesimple as zs
from pycobol import comportement as cp


import unittest  

class Testredefine(unittest.TestCase):
    def test_aln1(self):    
        obj2 = zn.ZoneIndependante( 'MADONNEE', 'X(5)')
        objr = zs.ZoneSimpleRedefine('MADONNE','REDEF1' ,5, picture = '9(5)')
        obj2.move_value('12')
        self.assertEqual (obj2.valeur_externe,'12   ')
