import sys
sys.path.insert(0, "../pycobol")
import unittest  
from pycobol import parser_cobol
from pycobol import execution


class TestStepMove(unittest.TestCase):

    def setUp(self):
        zg1 ='''        PROCEDURE DIVISION.
                            DISPLAY "Hello world !".'''
        zg2 ='''
                77    NOM PIC X(10).
                77    PRENOM PIC X(10).'''  
        tlignes = parser_cobol.fake_read_file(zg2)
        arbre =parser_cobol.read_groupe_from_code(tlignes)
        arbre.autonomme(globals())
        lignes_cobol = parser_cobol.fake_read_file_proc(zg1)
        self.pgm = parser_cobol.load_procedure(lignes_cobol)
        print('OK')

    def test_aln1(self):    
        _inst = execution.Instruction('move', ["ERIC", _prenom])
        self.pgm.add_step(_inst)
        _inst = execution.Instruction('move', [1234, _nom])
        self.pgm.add_step(_inst)
        self.pgm.run()
        self.assertEqual(_nom.valeur_externe,'1234      ')
        self.assertEqual(_prenom.valeur_externe,'ERIC      ')

if __name__ == '__main__':
    unittest.main()        