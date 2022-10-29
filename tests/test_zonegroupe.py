from pycobol import zonegroupe as zn 
from pycobol import comportement as cp

import unittest  

class TestZonegroupe(unittest.TestCase):
    def test_creation_groupe1(self):    
        obj_ = zn.ZoneGroupe('essai',1, 0)
        self.assertEqual (obj_.fils,[])
  