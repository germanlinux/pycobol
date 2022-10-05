with open('pic77.txt')  as file :
    with open('pic77ok.txt', 'w') as out:
        
        for ligne in file:
            lignet = re.match(r'(.*\.)', ligne)
            lignet = lignet[1]
            out.write(lignet + '\n')