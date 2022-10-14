from dataclasses import dataclass, field

@dataclass
class Comportement():
    ''' Permet de cadrer les variables de type ALN et NUM
        >>> obj = Comportement('ALN' , 10 , None, None , None)
        >>> obj.initialize()
        >>> obj.valeur_externe
        '          '
        >>> obj = Comportement('ALN' , 10 , 'eric', None , None)
        >>> obj.initialize()
        >>> obj.valeur_externe
        'eric      '
        >>> len(obj.valeur_externe)
        10
        >>> obj = Comportement('NUM' , 10 , None, None , None)
        >>> obj.initialize()
        >>> obj.valeur_externe
        '0000000000'
        >>> obj = Comportement('NUM' , 10 , 50, None , None)
        >>> obj.initialize()
        >>> obj.valeur_externe
        '0000000050'
        >>> len(obj.valeur_externe)
        10
        >>> obj = Comportement('SNUM' , 10 , None, None , None)
        >>> obj.initialize()
        >>> obj.valeur_externe
        '+0000000000'
        >>> obj = Comportement('SNUM' , 10 , -50, None , None)
        >>> obj.initialize()
        >>> obj.valeur_externe
        '-0000000050'
        >>> len(obj.valeur_externe)
        11
    '''    
    type_: str
    longueur: int
    valeur: str
    valeur_externe : str
    nature_valeur :str

    def __post_init__(self):
        if self.type_ in ['ALN', 'ALP'] :
            self.padding = ' '
            self.direction = 'left'
            self.defaut =''
        else:
            self.padding = '0'
            self.direction = 'right'
            self.defaut = 0
            
                

    def initialize(self):
        if self.valeur == None :
            self.valeur_externe = self.padding * self.longueur
            self.valeur = self.defaut

            if self.type_[0] == 'S' and self.valeur >= 0:
                self.valeur_externe = '+' + self.valeur_externe  
        else: 
            if self.direction == 'left':
                self.valeur_externe = str(self.valeur).ljust(self.longueur,self.padding)
            else:
                self.valeur_externe = str(abs(self.valeur)).rjust(self.longueur,self.padding) 
                if self.type_[0] == 'S' and self.valeur < 0:
                     self.valeur_externe = '-' + self.valeur_externe
                elif self.type_[0] == 'S' and self.valeur >= 0:
                     self.valeur_externe = '+' + self.valeur_externe  
              
    @classmethod
    def from_object(cls, obj ):
        ''' Methode de classe retournant un objet comportement à partir d'une instance de zone
            param: zone  objet zonage
        '''   
        return cls(obj.son_type , obj.longueur_interne, obj.value, obj.valeur_externe, obj.nature_value )


if __name__ == '__main__':  
    import doctest          
    doctest.run_docstring_examples(Comportement,None, verbose = 0)
    