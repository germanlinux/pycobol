import unittest  
import sys
sys.path.insert(0, "../pycobol")
#from arbrezone import Arbre
from parser_cobol import *
class Testfiller(unittest.TestCase):

    def test_aln6(self): 
        zg6 ='''
                10            MADATE PIC 9(8).
                    11            AAAA   PICTURE  9(4).                 
                    11            FILLER   PICTURE  99.                      
                    11            FILLER   PICTURE  99.'''      
        tlignes = fake_read_file(zg6)
        arbre =read_groupe_from_code(tlignes)
        self.assertEqual(3, len(arbre.zone[0].fils))  
        self.assertEqual('FILLER_MADATE', arbre.zone[2].nom)
        self.assertEqual('FILLER_MADATE_1', arbre.zone[3].nom)          