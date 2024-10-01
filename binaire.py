def binaire(entier, base):
    resultat = ""
    hexN = "0123456789ABCDEF"
    
    while entier > 0:
        rest = entier % base
        if base == 16:
            resultat = hexN[rest] + resultat
        else:
            resultat = str(rest) + resultat 
        entier = entier // base
    
    return resultat 

print(binaire(12054, 8))
