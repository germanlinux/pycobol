class DataFormatNotCompatible(Exception):
    '''Définition de nos propres Exceptions. Elle se déclenche si la donnée receptrice n'est pas 
    compatible avec la donnée emetrice. 
    exemple: faire un move d'un nombre flottant dans une zone alphanumérique.'''
    
    def __init__(self, nom):
        super().__init__(f"la donnée receptrice  <{nom}> n'est pas compatible avec la donnée emetrice")


class Constant:
    ''' cette classe fictive ne sert qu'a porter des attributs ajoutés manuellement
    Les objets ainsi crées se comporteront comme un véritable objet porteur de données.
    elle n'a ni methode ni attribut.
    Utilisation:
    e_ = Constant()
    e_.son_type ='ALN'
    e = e_
    '''
    pass

def controle_compatible(e, r):
    ''' cette fonction controle la compatibilité de nature des zones
    pour un move'''
    try : 
        emetteur_type = e.son_type
    except: 
        ## c est un type de base
        ## lequel ? : int, float , str ?
        if type(e) == str :
            e_ = Constant()
            e_.son_type ='ALN'
            e = e_
        if type(e) == float :
            e_ = Constant()
            e_.son_type ='FLOAT'
            e = e_
            

    if 'FLOAT' in e.son_type and 'FLOAT' in r.son_type:
        return True
    if 'ALN' in e.son_type and 'ALN' in r.son_type:
        return True
    if 'NUM' in e.son_type and 'NUM' in r.son_type:
        return True
    if 'GRP' in e.son_type and 'GRP' in r.son_type:
        return True    
    if 'ALN' in e.son_type and 'GRP' in r.son_type:
        return True
    if 'NUM' in e.son_type and 'GRP' in r.son_type:
        return True
        
    ## TODO tester la suite
    return False