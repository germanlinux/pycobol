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

    def test_p2(self):
        pgm = exe.Program('demo')
        inst = exe.Instruction('display', ['hello world'])
        pgm.add_step(inst) 
        self.assertEqual(len(pgm.vidage()),46)

    def test_p3(self):
        pgm = exe.Program('demo')
        inst = exe.Instruction('display', ['hello world'])
        pgm.add_step(inst) 
        inst = exe.Instruction('stop_run', [])
        pgm.add_step(inst)
        self.assertEqual(pgm.run(),None)

 
if __name__ == '__main__':
    unittest.main()