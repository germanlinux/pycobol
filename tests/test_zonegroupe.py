from pycobol import zonegroupe as zn 
from pycobol import comportement as cp

import unittest  

class TestZonegroupe(unittest.TestCase):
    def test_creation_groupe1(self):    
        obj_ = zn.ZoneGroupe('essai',1, 0)
        self.assertEqual (obj_.fils,[])
    
    def test_recurs1(self):
        obj_ = zn.ZoneGroupe('essai',1, 0)
        objfils = zn.ZoneGroupe('zonegrpfils', 2)
        obj_.ajout_fils_groupe(objfils)
        objfilsimp = zn.ZoneFilsSimple('essaifils', 5, picture = '999')
        obj_.ajout_fils_simple(objfilsimp)
        objfilsimp2 = zn.ZoneFilsSimple('essaifilssp', 5, picture = 'X(5)')
        objfils.ajout_fils_simple(objfilsimp2)
        obj_.maj_valeur()
        self.assertEqual (obj_.valeur_externe,"     000")