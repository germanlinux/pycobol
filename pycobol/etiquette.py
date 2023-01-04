from dataclasses import dataclass, field

@dataclass
class Etiquette():
    ''' Cette classe est destinée a définir des etiquettes comme dans les programmes COBOL
    avec la notion de paragraphe.

    '''
    nom: str
    instructions: list = []


@dataclass
class  Instruction():
    ''' Une instruction est un objet, une méthode et un ou plusieur parametres
    '''
    obj: object
    method: str
    arg: str 

    def display(self, qqchose, *args):
        if type(qqchose) == str :
            print(qqchose)
        elif type(qqchose) == list:
            pass

        return
                    
@dataclasses
class Program()    
    ''' squellette d'un programme
    '''
    pas_programme: list = []
    


