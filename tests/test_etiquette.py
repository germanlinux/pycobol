import sys
sys.path.insert(0, "../pycobol")
#from pycobol import arbrezone as arb
from unittest.mock import Mock 
from pycobol import execution as exe
import unittest  

class Testprogram(unittest.TestCase):
    def test_p1(self):
        pgm = exe.Program('demo')
        self.assertEqual(pgm.vidage(),'Etiquette:Debut_programme\n')
        
if __name__ == '__main__':
    unittest.main()