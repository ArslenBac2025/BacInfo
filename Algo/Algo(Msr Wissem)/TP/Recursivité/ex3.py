ch = "   aziz"

def espace(ch):
    if(ch[0] != " "):
        return ch
    return espace(ch[1:len(ch)])

print(espace(ch))