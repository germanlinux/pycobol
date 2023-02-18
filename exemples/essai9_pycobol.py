## essai de pycobol 
import sys
sys.path.insert(0, "../pycobol")
from pycobol import parser_cobol
zg1 ='''        PROCEDURE DIVISION.
                            DISPLAY "Hello world !".
                            STOP RUN.'''
zg2 ='''
                77    NOM PIC X(20).
        '''  
tlignes = zg.ZoneGroupe.fake_read_file(zg2)
len(tlignes)
arbre =zg.ZoneGroupe.read_groupe_from_code(tlignes)





lignes_cobol = parser_cobol.fake_read_file_proc(zg1)
pgm = parser_cobol.load_procedure(lignes_cobol)
print('Contenu')
print(pgm.vidage())
print('Execution')
pgm.run()
