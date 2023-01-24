## essai de pycobol 
import sys
sys.path.insert(0, "../pycobol")
from pycobol import execution as exe
### methode non structurée
pgm = exe.Program('demo')
print(pgm.vidage())
inst = exe.Instruction('display', ['hello world'])
pgm.pas_programme.append(inst)
inst = exe.Instruction('stop_run', [])
pgm.add_step(inst)

print(pgm.vidage()) 
pgm.run()
### Methode structurée
pgm2 = exe.Program('demo2')
print(pgm.vidage())
inst = exe.Instruction('display', ['hello world'])
pgm2.add
pgm.pas_programme.append(inst)
inst = exe.Instruction('stop_run', [])
pgm.pas_programme.append(inst)

print(pgm.vidage()) 
pgm.run()
