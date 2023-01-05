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
        ''' le format de qqchose :
        Une chaine de caractere ?  "eric"
        Un tuple ?: (nomcobol,"chaine", nomcobol2" ) etc''' 
 
        if type(qqchose) == str :
            print(qqchose)
        else:
            chaine = ""
            for item in qqchose:
                if type(item) == str :
                    chaine += item
                else:
                    chaine += item.valeur_externe
            print(chaine)            
        return None

@dataclasses
class Program()    
    ''' squellette d'un programme
    '''
    pas_programme: list = []
    


