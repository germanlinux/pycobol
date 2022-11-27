from pycobol import zonegroupe as zn 
from pycobol import comportement as cp
import sys
sys.path.insert(0, "../pycobol")
import unittest  

class TestSteptest(unittest.TestCase):
    def test_aln1(self):    
        obj2 = zn.ZoneIndependante( 'MADONNEE', 'X(5)')
        obj2.move_value('12')
        self.assertEqual (obj2.valeur_externe,'12   ')

    def test_aln2(self):    
        obj2 = zn.ZoneIndependante( 'MADONNEE', 'X(5)')
        obj2.move_value(12)
        self.assertEqual (obj2.valeur_externe,'12   ')

    def test_aln3(self):    
        obj2 = zn.ZoneIndependante( 'MANUM', '9(5)')
        obj2.move_value('eg')
        self.assertEqual (obj2.valeur_externe,'000eg')

    def test_aln4(self):    
        obj2 = zn.ZoneIndependante( 'MANUM', '9(5)')
        obj2.move_value('e')
        self.assertEqual (obj2.valeur_externe,'0000e')
    
    def test_aln5(self):    
        obj2 = zn.ZoneIndependante( 'MANUM', '9(5)')
        obj2.move_value('12')
        self.assertEqual (obj2.valeur_externe,'00012')

    def test_aln6(self):    
        obj2 = zn.ZoneIndependante( 'MANUM', '9(5)')
        obj2.move_value(12)
        self.assertEqual (obj2.valeur_externe,'00012')
    