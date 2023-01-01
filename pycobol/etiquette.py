from dataclasses import dataclass, field

@dataclass
class Etiquette():
    ''' Cette classe est destinée a définir des etiquettes comme dans les programmes COBOL
    avec la notion de paragraphe
    '''
    nom: str
    instructions: list = []
