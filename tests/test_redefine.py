import sys
sys.path.insert(0, "../pycobol")
from pycobol import zonesimple as zs
from pycobol import comportement as cp
from pycobol import arbrezone as arb
from pycobol import zonegroupe as zn  

import unittest  

class Testredefine(unittest.TestCase):
    def test_aln1(self):
        obj2 = zs.ZoneFilsSimple( 'MADONNEE',5, picture = 'X(5)')
        objr = zs.ZoneSimpleRedefine('MADONNEE','REDEF1' ,5, picture = '9(5)')
        obj2.move_value('12')
        self.assertEqual (obj2.valeur_externe,'12   ')
        self.assertEqual (objr.valeur_externe,'12   ')
                
    def test_aln2(self):
        zs.ZoneGroupe.reset_arbre()
        obj2 = zs.ZoneFilsSimple( 'MADONNEE',5, picture = 'X(5)')
        objr = zs.ZoneSimpleRedefine('MADONNEE','REDEF1' ,5, picture = '9(5)')
        objr.move_value('12')
        self.assertEqual (obj2.valeur_externe,'00012')
        self.assertEqual (objr.valeur_externe,'00012')   

    def test_aln3(self):    
        obj_ = zn.ZoneGroupe('essai',1, 0)
        objfilsimp = zs.ZoneFilsSimple('essaifils', 5, picture = '999')
        objfilsimp2 = zs.ZoneFilsSimple('essaifilssp', 5, picture = 'X(5)')
        objfilsimp3 = zs.ZoneFilsSimple('essaifils', 5, picture = '999')
        obj_.ajout_fils_simple(objfilsimp)
        obj_.ajout_fils_simple(objfilsimp2)
        obj_.ajout_fils_simple(objfilsimp3)
        objr = zs.ZoneSimpleRedefine('essaifils','REDEF1' ,5, picture = 'X(3)')
        obj_.init_groupe() 
        obj_.move_value('123ERICG456')
        print(objfilsimp3.valeur_externe)
        print(objfilsimp2.valeur_externe)
        objr.move_value(789)
        print(objfilsimp3.valeur_externe)
        

if __name__ == '__main__':
    unittest.main()