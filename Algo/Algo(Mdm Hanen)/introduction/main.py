
def somme(n):
    if n == 0:
        return 0
    
    return n + somme(n - 1)

def factoriel(n):
    if n == 0:
        return 1
    
    return n * factoriel(n - 1)

def somme_nombre(ch):
    if len(ch) == 0:
        return 0
    
    
    if ch[0].isnumeric():
        to_add = int(ch[0])
    else:
        to_add = 0
        
    return to_add + somme_nombre(ch[1:])

def main():
    ch = "Bac2024"
    res = somme_nombre(ch)
    print(res)

main()