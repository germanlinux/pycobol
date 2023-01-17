## essai de pycobol 
import sys
sys.path.insert(0, "../pycobol")
from pycobol import etiquette 
pgm = etiquette.Program('demo')
print(pgm.vidage())
inst = etiquette.Instruction('display', ['hello world'])
pgm.pas_programme.append(inst)
inst = etiquette.Instruction('stop_run', [])
pgm.pas_programme.append(inst)

print(pgm.vidage()) 
pgm.run()