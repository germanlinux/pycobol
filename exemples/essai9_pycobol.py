## essai de pycobol 
import sys
sys.path.insert(0, "../pycobol")
from pycobol import parser_cobol


zg1 ='''        PROCEDURE DIVISION.
                            DISPLAY "Hello world !".
                            STOP RUN.'''
zg2 ='''
                77    NOM PIC X(20).'''  
tlignes = parser_cobol.fake_read_file(zg2)
len(tlignes)
arbre =parser_cobol.read_groupe_from_code(tlignes)
arbre.autonomme(globals())
lignes_cobol = parser_cobol.fake_read_file_proc(zg1)
'''
pgm = parser_cobol.load_procedure(lignes_cobol)
print('Contenu')
print(pgm.vidage())

print('Execution')
pgm.run()
'''

pgm = exe.Program('demo')
print(pgm.vidage())
inst = exe.Instruction('accept', _NOM)
pgm.add_step(inst)
inst = exe.Instruction('stop_run', [])
pgm.add_step(inst)

print(pgm.vidage()) 
pgm.run()