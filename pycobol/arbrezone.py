class ArbreZone:
    ''' cette classe est in conteneur pour stocker des objets de 
        classe mere et de classe fille
        Elle implémente le pattern singleton
    >>> obj = ArbreZone()
    >>> obj.zone.append('1')
    >>> obj2 = ArbreZone()
    >>> print(obj2.zone)
    ['1']



    '''

    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(ArbreZone, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        try:
            self.zone
        except :    
            self.zone = []

if __name__ == '__main__':  
    import doctest          
    doctest.run_docstring_examples(ArbreZone,None, verbose = 1)