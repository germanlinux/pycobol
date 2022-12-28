from pycobol import zonegroupe as zn 
from pycobol import comportement as cp
from parser_cobol import *
import unittest  



zg1 = '''
10            WW04-DAECH.                                   
      11            WW04-AECH   PICTURE  9(4).                 
      11            WW04-MECH   PICTURE  99.                      
      11            WW04-JECH   PICTURE  99.                 
'''
zg2 = '''
10                  OC00.                                  
      11            OC00-CODS  PICTURE  X.               
      11            OC00-CODAP PICTURE  X(3).            
      11            OC00-COAS  PICTURE  X(6).            
      11            OC00-NPRO  PICTURE  XXX.             
      11            OC00-CODE  PICTURE  X.               
      11            OC00-COCOM PICTURE  9(3).            
      11            OC00-LIGNE  PICTURE  X(13).   
'''
zg3 = '''
10            OA00-IDNCN.                              
      11            OA00-NUPSI  PICTURE  X(15).              
      11            OA00-CNAEM  PICTURE  9(5).               
      11            OA00-NUPEN  PICTURE  X(9). 
'''  

zg4 = '''
10            OA00-IDNCN.                              
      11            OA00-NUPSI  PICTURE  X(15). 
      11            DEUXIEME.
      12            OA00-CNAEM  PICTURE  9(5).               
      12            OA00-NUPEN  PICTURE  X(9). 
'''  
zg5 = '''
10            OA00-IDNCN.                              
      11            OA00-NUPSI  PICTURE  X(15). 
      11            DEUXIEME.
       12            OA00-CNAEM  PICTURE  9(5).               
       12            OA00-NUPEN  PICTURE  X(9).
      11            troisieme.
       12            AAAA  PIC XXX     
'''  
zg6 = '''
10            OA00-IDNCN.                               
      11            DEUXIEME.
      12            OA00-CNAEM  PICTURE  9(5).               
      12            OA00-NUPEN  PICTURE  X(9). 
      11            troisieme.
      12            AAAA  PIC XXX       
'''  
zg7 = '''
10            OA00-IDNCN.                               
      11            DEUXIEME.
      12            OA00-CNAEM  PICTURE  9(5).               
      12            OA00-NUPEN  PICTURE  X(9). 
      11            troisieme.
      12            AAAA  PIC XXX.
      11            SIMPLE PIC 99.       
'''  
class TestZonegroupeline(unittest.TestCase):
      def test_lecture_groupe1(self):
            for cp, extrait in enumerate([zg1, zg2, zg3]):
                  tlignes = fake_read_file(extrait)
                  read_groupe_from_code(tlignes)
                  self.assertEqual (len(zn.ZoneGroupe.get_arbre()[0].fils),len(tlignes) - 1)
                  zn.ZoneGroupe.reset_arbre()

      def test_lecture_groupe2(self):
                  tlignes = fake_read_file(zg4)
                  read_groupe_from_code(tlignes)
                  self.assertEqual (len(zn.ZoneGroupe.get_arbre()[0].fils),2) 
                  self.assertEqual (len(zn.ZoneGroupe.get_arbre()[2].fils),2) 

      def test_lecture_groupe3(self):
                  zn.ZoneGroupe.reset_arbre()
                  tlignes = fake_read_file(zg5)
                  read_groupe_from_code(tlignes)
                  self.assertEqual (len(zn.ZoneGroupe.get_arbre()[0].fils),3) 
                  self.assertEqual (len(zn.ZoneGroupe.get_arbre()[2].fils),2) 
                  self.assertEqual (len(zn.ZoneGroupe.get_arbre()[5].fils),1) 

      def test_lecture_groupe4(self):
                  zn.ZoneGroupe.reset_arbre()
                  tlignes = fake_read_file(zg6)
                  read_groupe_from_code(tlignes)
                  self.assertEqual (len(zn.ZoneGroupe.get_arbre()[0].fils),2) 
                  self.assertEqual (len(zn.ZoneGroupe.get_arbre()[1].fils),2) 
                  self.assertEqual (len(zn.ZoneGroupe.get_arbre()[4].fils),1) 

      def test_lecture_groupe5(self):
                  zn.ZoneGroupe.reset_arbre()
                  tlignes = fake_read_file(zg7)
                  read_groupe_from_code(tlignes)
                  self.assertEqual (len(zn.ZoneGroupe.get_arbre()[0].fils),3) 
                  self.assertEqual (len(zn.ZoneGroupe.get_arbre()[1].fils),2) 
                  self.assertEqual (len(zn.ZoneGroupe.get_arbre()[4].fils),1) 
