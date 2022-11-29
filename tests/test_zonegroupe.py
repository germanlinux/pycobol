from pycobol import zonegroupe as zn 
from pycobol import zonesimple as zs 

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
        objfilsimp = zs.ZoneFilsSimple('essaifils', 5, picture = '999')
        obj_.ajout_fils_simple(objfilsimp)
        objfilsimp2 = zs.ZoneFilsSimple('essaifilssp', 5, picture = 'X(5)')
        objfils.ajout_fils_simple(objfilsimp2)
        obj_.maj_valeur()
        self.assertEqual (obj_.valeur_externe,"     000")

    def test_recurs2(self):
        obj_ = zn.ZoneGroupe('essai',1, 0)
        objfilsimp = zs.ZoneFilsSimple('essaifils', 5, picture = '999')
        objfilsimp2 = zs.ZoneFilsSimple('essaifilssp', 5, picture = 'X(5)')
        objfilsimp3 = zs.ZoneFilsSimple('essaifils', 5, picture = '999')
        obj_.ajout_fils_simple(objfilsimp)
        obj_.ajout_fils_simple(objfilsimp2)
        obj_.ajout_fils_simple(objfilsimp3)
        obj_.init_groupe()
        self.assertEqual (obj_.longueur_utile,11)    
        obj_.move_value('ERIC')
        self.assertEqual(obj_.valeur_externe,'ERIC       ')
        self.assertEqual(objfilsimp.valeur_externe,'ERI')
        self.assertEqual(objfilsimp2.valeur_externe,'C    ')
        self.assertEqual(objfilsimp3.valeur_externe,'   ')
        self.assertEqual(objfilsimp3.longueur_utile,3)

        obj_.move_value('tresgrandtropgrand')
        self.assertEqual(obj_.valeur_externe,'tresgrandtr')
        self.assertEqual(objfilsimp.valeur_externe,'tre')
        self.assertEqual(objfilsimp2.valeur_externe,'sgran')
        self.assertEqual(objfilsimp3.valeur_externe,'dtr')
        self.assertEqual(objfilsimp3.longueur_utile,3)
