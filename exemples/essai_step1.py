## essai de pycobol 
import sys
sys.path.insert(0, "../pycobol")
from pycobol import zonage as zn

obj2 = zn.ZoneIndependante( 'MADONNEE', 'X(5)')
obj3 = zn.ZoneIndependante( 'MANUM', '9(5)')
obj2.move_value(12)
print(obj2.valeur_externe)
obj2.move_value('12')
print(obj2.valeur_externe)
obj3.move_value('e')
print(obj3.valeur_externe)
obj3.move_value('eg')
print(obj3.valeur_externe)

'''

        IDENTIFICATION DIVISION.
        PROGRAM-ID. ESSAI1.
        ENVIRONMENT DIVISION.
        DATA DIVISION.
        WORKING-STORAGE SECTION.
          77 MADONNEE PIC X(5).
          77 MANUM PIC 9(5).
        PROCEDURE DIVISION.
             move  '12'  to MADONNEE.
             display MADONNEE.
             move  12  to MADONNEE.
             display MADONNEE.
             move  'e'  to MANUM.
             display MANUM.
             move  'eg'  to MANUM.
             display MANUM.
             
             STOP RUN.


      * 12   
      * 12   
      * 0000e
      * 000eg
'''      