def triangulaire(ch, i):
    if(i > len(ch)):
        return ""
    print(ch[0: i])
    return triangulaire(ch, i + 1)
    
triangulaire("aziz", 0)