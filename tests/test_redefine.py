import sys
sys.path.insert(0, "../pycobol")
from pycobol import zonesimple as zs
from pycobol import comportement as cp
from pycobol import arbrezone as arb

import unittest  

class Testredefine(unittest.TestCase):
    def test_aln1(self):
        obj2 = zs.ZoneFilsSimple( 'MADONNEE',5, picture = 'X(5)')
        objr = zs.ZoneSimpleRedefine('MADONNEE','REDEF1' ,5, picture = '9(5)')
        obj2.move_value('12')
        self.assertEqual (obj2.valeur_externe,'12   ')
        self.assertEqual (objr.valeur_externe,'12   ')
                
    def test_aln2(self):
        zs.ZoneGroupe.reset_arbre()
        obj2 = zs.ZoneFilsSimple( 'MADONNEE',5, picture = 'X(5)')
        objr = zs.ZoneSimpleRedefine('MADONNEE','REDEF1' ,5, picture = '9(5)')
        objr.move_value('12')
        self.assertEqual (obj2.valeur_externe,'00012')
        self.assertEqual (objr.valeur_externe,'00012')   



if __name__ == '__main__':
    unittest.main()