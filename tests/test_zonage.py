from pycobol import zonage as zn 
from pycobol import comportement as cp

import unittest  

class TestZonage(unittest.TestCase):

    def test_niveau77(self):    
        obj_ = zn.ZoneIndependante('essai','9(10)', None )
        self.assertEqual (obj_.valeur_interne ,0)
        self.assertEqual (obj_.valeur_externe ,'0000000000')
        obj_ = zn.ZoneIndependante('essai','X(4)', None )
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
        self.assertEqual (obj_.valeur_interne ,'er')
        self.assertEqual (obj_.valeur_externe ,'er  ')   


    def test_77_classmethod_comportement1(self):                
        ligne = "77 CTS01     PIC  9(4)  VALUE ZERO."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        objc_ = cp.Comportement.from_object(obj_)
        self.assertEqual(obj_.son_type, 'NUM')
        self.assertEqual(obj_.longueur_utile, 4)
    
    def test_77_move_valeur_comportement2(self):                
        ligne = "77 CTS01     PIC  X(10)  VALUE '1234567890'."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        objc_ = cp.Comportement.from_object(obj_)
        objc_.move_value(obj_ ,'ERIC')
        self.assertEqual(obj_.valeur_externe, 'ERIC567890')
        self.assertEqual(obj_.longueur_utile, 10)

    def test_77_move_valeur_comportement3(self):                
        ligne = "77 CTS01     PIC  X(10)  VALUE '1234567890'."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        objc_ = cp.Comportement.from_object(obj_)
        objc_.move_value(obj_, 'ERICXXXXXXXXXXXXXX')
        self.assertEqual(obj_.valeur_externe, 'ERICXXXXXX')
        self.assertEqual(obj_.longueur_utile, 10)
    
    def test_77_move_valeur_comportement4(self):                
        ligne = "77 CTS01     PIC  9(6)  VALUE 100."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        objc_ = cp.Comportement.from_object(obj_)
        objc_.move_value(obj_,3000)
        self.assertEqual(obj_.valeur_externe, '003000')
        self.assertEqual(obj_.longueur_utile, 6)

    def test_77_move_valeur_comportement5(self):                
        ligne = "77 CTS01     PIC  9(6)  VALUE 100."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        objc_ = cp.Comportement.from_object(obj_)
        objc_.move_value(obj_,1234567)
        self.assertEqual(obj_.valeur_externe, '234567')
        self.assertEqual(obj_.longueur_utile, 6)

    def test_77_move_valeur_comportement6(self):                
        ligne = "77 CTS01     PIC  S9(6)  VALUE -100."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        objc_ = cp.Comportement.from_object(obj_)
        objc_.move_value(obj_,1234567)
        self.assertEqual(obj_.valeur_externe, '+234567')
        self.assertEqual(obj_.longueur_utile, 6)

    def test_77_classmethod_comportement101(self):                
        ligne = "77 CTS0101     PIC  9(4)V99."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        self.assertEqual(obj_.son_type, 'FLOAT')
        self.assertEqual(obj_.longueur_utile, 6)

    def test_77_classmethod_comportement200(self):                
        ligne = "77 CTS0101     PIC  9(4)V99 VALUE ZERO."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        self.assertEqual(obj_.son_type, 'FLOAT')
        self.assertEqual(obj_.valeur_externe, '0000,00')
    
    def test_77_classmethod_comportement201(self):                
        ligne = "77 CTS0101     PIC  9(4)V99 VALUE 1234,56."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        self.assertEqual(obj_.son_type, 'FLOAT')
        self.assertEqual(obj_.valeur_externe, '1234,56')
    def test_77_classmethod_comportement202(self):                
        ligne = "77 CTS0101     PIC  9(4)V99 VALUE 123456,56."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        self.assertEqual(obj_.son_type, 'FLOAT')
        self.assertEqual(obj_.valeur_externe, '3456,56')
    def test_77_classmethod_comportement203(self):                
        ligne = "77 CTS0101     PIC  9(4)V99 VALUE 1234,5678."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        self.assertEqual(obj_.son_type, 'FLOAT')
        self.assertEqual(obj_.valeur_externe, '1234,78')
    def test_77_classmethod_comportement303(self):                
        ligne = "77 CTS0101     PIC  XXXX VALUE 'ABCDEFGH."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        self.assertEqual(obj_.son_type, 'ALN')
        self.assertEqual(obj_.valeur_externe, 'ABCD')
    
    def test_77_classmethod_comportement304(self):                
        ligne = "77 CTS0101     PIC  XXXX VALUE 99421."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        self.assertEqual(obj_.son_type, 'ALN')
        self.assertEqual(obj_.valeur_externe, '9942')



