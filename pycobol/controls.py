class Constant:
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