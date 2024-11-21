def binaire(entier, base):
    resultat = ""
    # Make a string that acts like an array
    hexN = "0123456789ABCDEF"
    # while the number can still be divided
    while entier > 0:
        rest = entier % base
        if base == 16:
            resultat = hexN[rest] + resultat
        else:
            resultat = str(rest) + resultat 
        entier = entier // base
    return resultat 

print(binaire(12054, 8))
