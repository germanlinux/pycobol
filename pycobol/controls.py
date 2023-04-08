def controle_compatible(e, r):
    ''' cette fonction controle la compatibilité de nature des zones
    pour un move'''
    try : 
        emetteur_type = e.son_type
    except: 
        ## c est un type de base
        ## lequel 
        

    if 'FLOAT' in a.son_type and 'FLOAT' in b.son_type:
        return True
    if 'ALN' in a.son_type and 'ALN' in b.son_type:
        return True
    if 'NUM' in a.son_type and 'NUM' in b.son_type:
        return True
    if 'GRP' in a.son_type and 'GRP' in b.son_type:
        return True    
    if 'ALN' in a.son_type and 'GRP' in b.son_type:
        return True
    if 'NUM' in a.son_type and 'GRP' in b.son_type:
        return True
        
    ## TODO tester la suite
    return False