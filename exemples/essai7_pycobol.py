## essai de pycobol 
import sys
sys.path.insert(0, "../pycobol")
from pycobol import execution as exe
pgm = exe.Program('demo')
print(pgm.vidage())
inst = exe.Instruction('display', ['hello world'])
pgm.pas_programme.append(inst)
inst = exe.Instruction('stop_run', [])
pgm.pas_programme.append(inst)

print(pgm.vidage()) 
pgm.run()