from pycobol import zonage as zn 
from pycobol import comportement as cp

import unittest  

class TestZonage(unittest.TestCase):

    def test_niveau77(self):    
        obj_ = zn.ZoneIndependante('essai','9(10)', None , None)
        self.assertEqual (obj_.value ,0)
        self.assertEqual (obj_.valeur_externe ,'0000000000')
        obj_ = zn.ZoneIndependante('essai','X(4)', None , None)
        self.assertEqual (obj_.value ,'')
        self.assertEqual (obj_.valeur_externe ,'    ')


    def test_77_avec_value(self):                
        ligne = "77 CTS01     PIC  9(4)  VALUE ZERO."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        self.assertEqual (obj_.value ,0)
        self.assertEqual (obj_.valeur_externe ,'0000')
        ligne = "77 CTS01     PIC  XXXX  VALUE SPACE."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        self.assertEqual (obj_.value ,'')
        self.assertEqual (obj_.valeur_externe ,'    ')            
        ligne = "77 CTS01     PIC  9(4)  VALUE 80."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        self.assertEqual (obj_.value ,80)
        self.assertEqual (obj_.valeur_externe ,'0080')
        ligne = "77 CTS01     PIC  XXXX  VALUE \"er\"."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        self.assertEqual (obj_.value ,'er')
        self.assertEqual (obj_.valeur_externe ,'er  ')            

    def test_77_classmethod_comportement(self):                
        ligne = "77 CTS01     PIC  9(4)  VALUE ZERO."
        obj_ = zn.ZoneIndependante.from_ligne(ligne)
        objc_ = cp.Comportement.from_object(obj_)
        self.assertEqual(objc_.type_, 'NUM')
        self.assertEqual(objc_.longueur, 4)
