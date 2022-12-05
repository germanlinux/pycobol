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
        zs.ZoneGroupe.reset_arbre()   
        obj_ = zn.ZoneGroupe('essai',1, 0)
        objfilsimp = zs.ZoneFilsSimple('essaifils1', 5, picture = '999')
        objfilsimp2 = zs.ZoneFilsSimple('essaifilssp', 5, picture = 'X(5)')
        objfilsimp3 = zs.ZoneFilsSimple('essaifils', 5, picture = '999')
        obj_.ajout_fils_simple(objfilsimp)
        obj_.ajout_fils_simple(objfilsimp2)
        obj_.ajout_fils_simple(objfilsimp3)
        objr = zs.ZoneSimpleRedefine('essaifils','REDEF1' ,5, picture = 'X(3)')
        obj_.init_groupe() 
        obj_.move_value('123ERICG456')
        objr.move_value(789)
        self.assertEqual('789', objr.valeur_externe)
        self.assertEqual('789', objfilsimp3.valeur_externe)
        self.assertEqual(obj_.valeur_externe,'123ERICG789' )

    def test_aln4(self): 
        zs.ZoneGroupe.reset_arbre() 
        obj = zs.ZoneFilsSimple('essaifils', 5, picture = '99999999')
        obj2 = zs.ZoneGroupeRedefine('essaifils', 'essairedefines' ,5) 
        objj = zs.ZoneFilsSimple('jj', 6, picture = '99')
        objmm = zs.ZoneFilsSimple('mm', 6, picture = '99')
        objaa = zs.ZoneFilsSimple('aaaa', 6, picture = '9999')
        obj2.ajout_fils_simple(objj)
        obj2.ajout_fils_simple(objmm)
        obj2.ajout_fils_simple(objaa)
        obj2.init_groupe()
        obj.move_value('10092022')
        print(zs.ZoneGroupe.vidage())
        self.assertEqual('10092022', obj2.valeur_externe )
        self.assertEqual('10', objj.valeur_externe)
        self.assertEqual('09', objmm.valeur_externe)
        self.assertEqual('2022', objaa.valeur_externe )
        
if __name__ == '__main__':
    unittest.main()