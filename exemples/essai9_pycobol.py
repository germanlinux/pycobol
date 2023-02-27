## essai de pycobol 
import sys
sys.path.insert(0, "../pycobol")
from pycobol import parser_cobol
from pycobol import execution

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

pgm = execution.Program('demo')
_inst = execution.Instruction('display', ["saisir votre nom"])
pgm.add_step(_inst)
_inst = execution.Instruction('accept', [_nom])
pgm.add_step(_inst)
_inst = execution.Instruction('display', ["bonjour ", _nom])
pgm.add_step(_inst)
_inst = execution.Instruction('stop_run', [])
pgm.add_step(_inst)

print(pgm.vidage()) 
pgm.run(mode =1)