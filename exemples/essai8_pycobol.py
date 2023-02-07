## essai de pycobol 
import sys
sys.path.insert(0, "../pycobol")
from pycobol import parser_cobol
zg1 ='''        PROCEDURE DIVISION.
                            DISPLAY "Hello world !".
                            STOP RUN.'''

lignes_cobol = parser_cobol.fake_read_file_proc(zg1)
pgm = parser_cobol.load_procedure(lignes_cobol)
print(pgm.vidage())
pgm.run()
