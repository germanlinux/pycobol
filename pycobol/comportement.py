from dataclasses import dataclass, field

@dataclass
class Comportement():
    type: str
    longueur: int
    valeur: str
    valeur_externe : str
    nature_valeur :str

@dataclass
class Comportement_aln(Comportement):
    ''' Permet de cadrer les variable de type ALN 
        >>> obj = Comportement_aln('ALN' , 10 , None, None , None)
        >>> obj.initialize()
        >>> obj.valeur_externe
        '          '
        >>> obj = Comportement_aln('ALN' , 10 , 'eric', None , None)
        >>> obj.initialize()
        >>> obj.valeur_externe
        'eric      '
        >>> len(obj.valeur_externe)
        10
    '''
    def __init__(self, *args ):
        self.cadrage = 'LEFT'
        super().__init__(*args)

    def initialize(self):
        if self.valeur == None :
            self.valeur_externe = ' ' * self.longueur
        else: 
            self.valeur_externe = self.valeur
            self.valeur_externe = self.valeur.ljust(self.longueur,' ')    
        
if __name__ == '__main__':  
    import doctest          
    doctest.run_docstring_examples(Comportement_aln,None, verbose = False)