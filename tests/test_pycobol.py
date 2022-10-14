from pycobol import __version__
from pycobol import zonage as zn
import unittest  

class TestStringMethods(unittest.TestCase):
    def test_version(self):
        assert __version__ == '0.1.0'

    def test_niveau77(self):
        with open('./tests/pic77ok.txt') as file:
            for ligne in file:
                with self.subTest(ligne = ligne):
                    ligne= ligne[:-1]
                    tabl = ligne.split('#')
                    obj_ = zn.ZoneIndependante.from_ligne(tabl[0])
                    self.assertEqual (tabl[1], obj_.son_type)
                    self.assertEqual (int(tabl[2]), obj_.longueur_interne)

                    if obj_.nature_value == 'NUM':
                        val_ = int(tabl[3])
                    else:
                        val_ = tabl[3]
                        if val_.isspace():
                            val_=''
                    if tabl[3] == 'None' :
                        val_= None
                    
    def test_niveau77_init(self):
        with open('./tests/pic77init.txt') as file:
            for ligne in file:
                with self.subTest(ligne = ligne):
                    ligne= ligne[:-1]
                    tabl = ligne.split('#')
                    obj_ = zn.ZoneIndependante.from_ligne(tabl[0])
                    obj_.initialize()
                    val_ = tabl[1]
                    if val_.isspace():
                            val_=''
                    else:
                         val_ = int(val_)        
                    if val_ == 'None' :
                        val_= ''
                    self.assertEqual (val_, obj_.value)
