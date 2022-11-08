from pycobol import zonegroupe as zn 
from pycobol import comportement as cp

import unittest  



zg1 ='''
10            WW04-DAECH.                                   
      11            WW04-AECH   PICTURE  9(4).                 
      11            WW04-MECH   PICTURE  99.                      
      11            WW04-JECH   PICTURE  99.                 
'''
zg2 ='''
10                  OC00.                                  
      11            OC00-CODS  PICTURE  X.               
      11            OC00-CODAP PICTURE  X(3).            
      11            OC00-COAS  PICTURE  X(6).            
      11            OC00-NPRO  PICTURE  XXX.             
      11            OC00-CODE  PICTURE  X.               
      11            OC00-COCOM PICTURE  9(3).            
      11            OC00-LIGNE  PICTURE  X(13).   
'''
zg3= '''
10            OA00-IDNCN.                              
      11            OA00-NUPSI  PICTURE  X(15).              
      11            OA00-CNAEM  PICTURE  9(5).               
      11            OA00-NUPEN  PICTURE  X(9). 
'''  
class TestZonegroupeline(unittest.TestCase):
      def test_lecture_groupe1(self):
            for cp, extrait in enumerate([zg1, zg2, zg3]):
                  tlignes = zn.ZoneGroupe.fake_read_file(extrait)
                  zn.ZoneGroupe.read_groupe_from_code(tlignes)
                  self.assertEqual (len(zn.ZoneGroupe.zone_groupe[cp].fils),len(tlignes) - 1) 
