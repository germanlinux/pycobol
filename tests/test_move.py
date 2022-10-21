import unittest  
from pycobol import zonage as zn
from pycobol import comportement as cp

class TestMove(unittest.TestCase):

    def test_niveaumove77_01(self):                
       ligne = "77 CTS0101     PIC  S9(4)V99 VALUE +1234,5678."
       obj_ = zn.ZoneIndependante.from_ligne(ligne)
       self.assertEqual(obj_.son_type, 'SFLOAT')
       self.assertEqual(obj_.valeur_externe, '+1234,78') 
       objcomp = cp.ComportementFloat.from_object(obj_)
       objcomp.move_value(obj_ , 25)
       self.assertEqual(obj_.valeur_externe, '+0025,00')
       self.assertEqual(obj_.valeur_interne, 25.0) 

    def test_niveaumove77_02(self):                
       ligne = "77 CTS0101     PIC  S9(4)V99 VALUE +1234,5678."
       obj_ = zn.ZoneIndependante.from_ligne(ligne)
       self.assertEqual(obj_.son_type, 'SFLOAT')
       self.assertEqual(obj_.valeur_externe, '+1234,78') 
       objcomp = cp.ComportementFloat.from_object(obj_)
       objcomp.move_value(obj_ , -25)
       self.assertEqual(obj_.valeur_externe, '-0025,00')
       self.assertEqual(obj_.valeur_interne, -25.0)    