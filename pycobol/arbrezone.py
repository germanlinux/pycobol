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
    _instance = None

    def __new__(cls, *args):
        if not cls._instance:
          #  if not hasattr(cls, 'instance'): 
          cls._instance = super(ArbreZone, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, *args):
        try:
            self.zone
        except :    
            self.zone = []
        finally:
           print('TOTO', len(self.zone))    
    def recherche_nom(self, nom):
        ''' retourne l'objet Zonegroupe ou ZonefilsSimple correpondant au nom 
        :nom str

        >>> tlignes = ZoneGroupe.fake_read_file()
        >>> len(tlignes)
        4
        >>> ZoneGroupe.read_groupe_from_code(tlignes)
        >>> len(ZoneGroupe.zone_groupe[0].fils)
        3
        >>> z1 = ZoneGroupe.recherche_nom('DAECH')
        >>> z1.longueur_utile
        8
        >>> z2 = ZoneGroupe.recherche_nom('JECH')
        >>> z2.longueur_utile
        2


        '''
        for item in self.zone:
            if item.nom == nom: 
                return item

        for item in   self.zone:
            for fils in item.fils:
                if fils.nom == nom:
                    return fils 
        return None
    

    def autonomme(self, glob ):
        for item in self.zone:
            glob['_' + item.nom] = item      


    def recherche_rang(self, n):
        a = self.zone[:]
        a.reverse()
        for item in a:
            if n > item.rang:
                return item
            if n == item.rang:
                return item.pere
        return a[-1]

               

if __name__ == '__main__':  
    import doctest          
    doctest.run_docstring_examples(ArbreZone,None, verbose = 1)