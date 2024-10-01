chemin = "decomp.txt"

def saisie():
    q = int(input("entrer q"))
    p = int(input("enter p"))
    while(not( p < q and q < 10000 and p > 10 )):
        q = int(input("entrer q"))
        p = int(input("enter p"))

    return p,q

def remplir(p, q):
    f = open(chemin, "w")
    f.write(str(str(p) + ' ' + str(q) + '\n'))

    np, nq, offset, k = p, q, 0, 2
    temp = ""

    while(nq != np):
        temp = str(np) + '='
        while(k < np):
            if(np % k == 0):
                temp+= str(k) + '*'
                np = np//k
                k = 2
            else:
                k+=1
        if(np != 1):
            temp += str(np)
        offset += 1
        np = p + offset
        k = 2
        f.write(temp + '\n')
        temp = ""
    f.close()

def afficher():
    f = open(chemin, "r")
    ch = f.readline()
    while(ch):
        print(ch[:len(ch) - 1])
        ch = f.readline()
    f.close()

p, q = saisie()
remplir(p, q)
afficher()


