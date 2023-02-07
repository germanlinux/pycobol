## essai de pycobol 
import sys
sys.path.insert(0, "../pycobol")
from pycobol import parser_cobol
lignes_cobol = parser_cobol.fake_read_file_proc()
pgm = parser_cobol.load_procedure(lignes_cobol)


