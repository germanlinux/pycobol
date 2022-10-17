from pycobol import zonage as zn 
from pycobol import comportement as cp

import unittest  

class TestZonage(unittest.TestCase):

    def test_niveau77(self):    
        obj_ = zn.ZoneIndependante('essai','9(10)', None , None)
        self.assertEqual (obj_.valeur_interne ,0)
        self.assertEqual (obj_.valeur_externe ,'0000000000')
        obj_ = zn.ZoneIndependante('essai','X(4)', None , None)
        self.assertEqual (obj_.valeur_interne ,'')
        self.assertEqual (obj_.valeur_externe ,'    ')


    def test_77_avec_value(self):                
        ligne = "77 CTS01     PIC  9(4)  VALUE ZERO."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        self.assertEqual (obj_.valeur_interne ,0)
        self.assertEqual (obj_.valeur_externe ,'0000')
        ligne = "77 CTS01     PIC  XXXX  VALUE SPACE."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        self.assertEqual (obj_.valeur_interne ,'')
        self.assertEqual (obj_.valeur_externe ,'    ')            
        ligne = "77 CTS01     PIC  9(4)  VALUE 80."

        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        self.assertEqual (obj_.valeur_interne ,80)
        self.assertEqual (obj_.valeur_externe ,'0080')
                 
        
    def test_77_avec_value_litt(self):
        ligne = "77 CTS01     PIC  XXXX  VALUE \"er\"."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        self.assertEqual (obj_.valeur_interne ,'erHHH')
        self.assertEqual (obj_.valeur_externe ,'er  ')   


    def test_77_classmethod_comportement1(self):                
        ligne = "77 CTS01     PIC  9(4)  VALUE ZERO."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        objc_ = cp.Comportement.from_object(obj_)
        self.assertEqual(objc_.type_, 'NUM')
        self.assertEqual(objc_.longueur, 4)
    
    def test_77_move_valeur_comportement2(self):                
        ligne = "77 CTS01     PIC  X(10)  VALUE '1234567890'."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        objc_ = cp.Comportement.from_object(obj_)
        objc_.move_value('ERIC')
        self.assertEqual(objc_.valeur_externe, 'ERIC567890')
        self.assertEqual(objc_.longueur, 10)

    def test_77_move_valeur_comportement3(self):                
        ligne = "77 CTS01     PIC  X(10)  VALUE '1234567890'."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        objc_ = cp.Comportement.from_object(obj_)
        objc_.move_value('ERICXXXXXXXXXXXXXX')
        self.assertEqual(objc_.valeur_externe, 'ERICXXXXXX')
        self.assertEqual(objc_.longueur, 10)
    
    def test_77_move_valeur_comportement4(self):                
        ligne = "77 CTS01     PIC  9(6)  VALUE 100."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        objc_ = cp.Comportement.from_object(obj_)
        objc_.move_value(3000)
        self.assertEqual(objc_.valeur_externe, '003000')
        self.assertEqual(objc_.longueur, 6)

    def test_77_move_valeur_comportement5(self):                
        ligne = "77 CTS01     PIC  9(6)  VALUE 100."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        objc_ = cp.Comportement.from_object(obj_)
        objc_.move_value(1234567)
        self.assertEqual(objc_.valeur_externe, '234567')
        self.assertEqual(objc_.longueur, 6)

    def test_77_move_valeur_comportement6(self):                
        ligne = "77 CTS01     PIC  S9(6)  VALUE -100."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        objc_ = cp.Comportement.from_object(obj_)
        objc_.move_value(1234567)
        self.assertEqual(objc_.valeur_externe, '+234567')
        self.assertEqual(objc_.longueur, 6)

