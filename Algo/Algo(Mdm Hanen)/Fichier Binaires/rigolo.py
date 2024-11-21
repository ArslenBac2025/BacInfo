from pickle import load, dump

e = dict()

def remplir():
    f = open("nombres.dat", "wb")
    for i in range(1, 1001):
        dump(i, f)


def facteur(num):
    val = int(num)
    i = 2
    res = ""
    while(i < val):
        if(val % i == 0):
            res += str(i) + "*"
            val = val // i
            i = 2
        else:
            i+=1
    return res + str(val)
def isRigolo(num):
    s1 = 0
    numstr = str(num)
    for i in range(len(numstr)):
        s1+= int(numstr[i])

    facteur_num = facteur(num)
    s2 = 0
    for i in range(len(facteur_num)):
        if(facteur_num[i].isnumeric()):
            s2 += int(facteur_num[i])

    return s1==s2


def stocker():
    fr = open("nombres.dat", "rb")
    fw = open("rigolo.dat", "wb")
    for i in range(1000):
        num = load(fr)
        if(isRigolo(num)):
            e["valeur"] = num
            e["facteur"] = facteur(num)
            dump(e, fw)
    fr.close()
    fw.close()
def afficher():
    f = open("rigolo.dat", "rb")
    while True:
        try:
            x = load(f)
            print(x["valeur"])
            print(x["facteur"])
        except:
            break
    f.close()

remplir()
stocker()
afficher()