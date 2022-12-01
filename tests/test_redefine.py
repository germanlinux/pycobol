import sys
sys.path.insert(0, "../pycobol")
from pycobol import zonesimple as zs
from pycobol import comportement as cp
from pycobol import arbrezone as arb

import unittest  

class Testredefine(unittest.TestCase):
    def test_aln1(self):
        arbre = arb.ArbreZone()
        obj2 = zs.ZoneFilsSimple( 'MADONNEE',5, picture = 'X(5)')
        objr = zs.ZoneSimpleRedefine('MADONNEE','REDEF1' ,5, picture = '9(5)')
        obj2.move_value('12')
        self.assertEqual (obj2.valeur_externe,'12   ')
        

if __name__ == '__main__':
    unittest.main()