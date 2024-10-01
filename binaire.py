def binaire(entier, base):
    resultat = ""
    hex_digits = "0123456789ABCDEF"
    
    while entier > 0:
        rest = entier % base
        if base == 16:
            resultat = hex_digits[rest] + resultat
        else:
            resultat = str(rest) + resultat 
        entier = entier // base
    
    return resultat 

print(binaire(12054, 8))