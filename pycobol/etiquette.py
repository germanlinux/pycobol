from dataclasses import dataclass, field

@dataclass
class Etiquette:
    ''' Cette classe est destinée a définir des etiquettes comme dans les programmes COBOL
    avec la notion de paragraphe.

    '''
    nom: str
    instructions: str =''

    def add_instruction(self, instruction):
        self.instructions.append(instruction)


    def recherche_nom(self, nom):
        for item in self.instructions:
            if item.nom == nom:
                return item
        else:
            return None            

@dataclass
class  Instruction():
    ''' Une instruction est un objet, une méthode et un ou plusieur parametres
    '''
    nom:str =''
    arg : str = ''

    def display(self, liste):
        '''
        :param liste: un ou plusieurs textes / objets a afficher
        :type liste: list  

        >>> from minimock import Mock
        >>> ZoneIndependante= Mock('ZoneIndependante')
        >>> ZoneIndependante.mock_returns = Mock('ZoneIndependante', valeur_externe = '00012'  )
        >>> data1 = ZoneIndependante('MADATA')
        ...
        >>> data1.valeur_externe
        '00012'
        >>> a = Instruction()
        >>> a.display(["essai"])
        essai
        True
        >>> a.display([data1])
        00012
        True
        >>> a.display([data1,' essai'] )
        00012 essai
        True
        '''

        qqchose = liste
        chaine = ""
        for item in qqchose:
                if type(item) == str :
                    chaine += item
                else:
                    chaine += item.valeur_externe
        print(chaine)            
        return True

    def stop_run(self):
        return False


@dataclass
class Program():   
    ''' squellette d'un programme

    >>> pgm = Program('demo')
    >>> pgm.vidage() # doctest: +ELLIPSIS
    '...'
    >>> inst = Instruction('display', ['hello world'])
    >>> pgm.pas_programme.append(inst)
    >>> pgm.vidage() # doctest: +ELLIPSIS
    '...'
    pgm.run()
    '''
    nom: str = 'default'
    pas_programme: str  =''

    def __post_init__(self):
        _et = Etiquette('Debut_programme', [])
        self.pas_programme = []
        self.add_etiquette(_et)

    def add_etiquette(self, etape):
        self.pas_programme.append(etape)

    def vidage(self):
        ''' retourne une chaine de caractère contenant la liste des etiquettes d'un programme
        '''
        _chaine =''
        for item in self.pas_programme:
            if type(item) == Etiquette:
                _chaine += f'Etiquette:{item.nom}\n'
            else: 
                _chaine += f'instruction:{item.nom}\n'
        return _chaine        

    def run(self):
        for item in self.pas_programme:
            ### execute instruction
            if type(item) == Etiquette:
                print('Etiquette:', item.nom)
            else:
                if item.arg:    
                    exe = getattr(item, item.nom)
                    res = exe(item.arg)
                else:
                    res = exe()
                    
                if res is False: 
                    break



    
if __name__ == '__main__':  
    import doctest          
    #doctest.run_docstring_examples(Instruction.display,None, verbose = 1)
    doctest.testmod()

