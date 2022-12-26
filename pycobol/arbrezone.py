from collections import defaultdict

class ArbreZone:
    ''' cette classe est un conteneur pour stocker des objets de 
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
            self.inverse = []
            self.redefine= {}
            self.inv_redefine= {}
        finally:
           pass

    def reset(self):
        ''' Remise à zero de toutes les structures'''

        self.zone =[]
        self.inverse = []
        self.redefine= {}
        self.inv_redefine= {}

    def recherche_nom(self, nom):
        ''' retourne l'objet Zonegroupe ou ZonefilsSimple correpondant au nom 
        
        :param nom: Attribut 'nom' de l'objet
        :type nom: str
        :return: Un objet :class:`pycobol.ZoneGroupe` ou :class:`pycobol.ZoneFilsSimple`  ou `None` 

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
            glob['_' + item.nom.lower()] = item      


    def recherche_rang(self, n):
        ''' On essaye de trouver le rang COBOL (niveau) de l'element supérieur
        
        La valeur 0 est retournée par defaut.

        :param n: rang de l'element en cours de traitement
        :type n: int
        :return: niveau superieur ou `0` '''

        a = self.zone[:]
        a.reverse()
        for item in a:
            if n > item.rang:
                return item
            if n == item.rang:
                return item.pere
        if len(a) > 1 :       
            return a[-1]
        else:
             return  0   
    def retroArbre(self):
        ''' Reconstitution des dependances des zones en partant des zones élémentaires
        
        '''
        self.inverse = defaultdict(list)
        for item in self.zone:
            try:
                if item.fils: 
                   for _fils in item.fils:
                        self.inverse[_fils.nom].append(item.nom)
            except:
                pass 
         
        for cle,value  in  self.inverse.items():
            for _fils in value:
                 if _fils in self.inverse:
                        self.inverse[cle].extend(self.inverse[_fils])
                        break

    def vidage(self):
        ''' Retourne la liste des zones et la liste des zones redefinis

        :return: un tuple de deux listes
        :rtype: tuple(list, list)
        '''
         
        _liste= []
        for item in self.zone:
            _liste.append(item.nom )
        _lref = list(self.redefine.keys())    
        return _liste, _lref
            

if __name__ == '__main__':  
    import doctest          
    doctest.run_docstring_examples(ArbreZone,None, verbose = 1)