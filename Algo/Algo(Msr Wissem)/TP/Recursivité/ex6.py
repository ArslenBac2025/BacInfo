def reverse(ch):
    if(ch == ""):
        return ch
    return ch[len(ch) - 1] + reverse(ch[0: len(ch) - 1])
    
def recherche(ch, c):
    if(ch == ''):
        return False
    elif(ch[0] == c):
        return True
    else:
        return recherche(ch[1: len(ch) - 1], c)
    
print(reverse("adem"))
print(recherche("adem", 'b'))