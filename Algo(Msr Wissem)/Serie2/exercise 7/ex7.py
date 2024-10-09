nphy1 = "text1.txt"
nphy2 = "text2.txt"
nphy3 = "text3.txt"


def saisie():
    n = int(input("n"))
    while(not(2 <= n <= 20)):
        n = int(input("n"))
    return n
def remplir():
    f = open(nphy1 , "w")
    for i in range(n):
        string = str(input("your sentence>>"))
        f.write(string + '\n')

    f.close()

def operation(ch):
    while(ch[0] == ' '):
        ch = ch[1:]

    while(ch[len(ch) - 1]  == ' '):
        ch = ch[:len(ch) - 1]

    nv_ch = ""
    for i in range(0, len(ch)):
        if(not(ch[i-1] == ' ' and ch[i-1] == ch[i])):
            nv_ch += ch[i]
    return str(nv_ch)

def stocker():
    fr = open(nphy1, "r")
    fw = open(nphy2, "w")

    ch = fr.readline()
    while(ch != ''):
        nvch = operation(ch[:len(ch) - 1])
        fw.write(nvch + '\n')
        ch = fr.readline()

    fr.close()
    fw.close()

def numeroter(ch, ligne):
    nvch = str(ligne) + " "
    for i in range(len(ch) - 1, -1, -1):
        nvch += ch[i]
    return nvch
def compter_mots(ch):
    compteur = 1
    for i in range(len(ch)):
        if(ch[i] == ' '): compteur +=1

    return compteur

def stocker2():
    fr = open(nphy2, "r")
    fw = open(nphy3, "w")


    compteur_mots = 0
    ligne = 1
    ch = fr.readline()
    while(ch != ''):
        nvch = numeroter(ch[:len(ch) - 1], ligne)
        compteur_mots += compter_mots(ch[:len(ch) - 1])
        fw.write(nvch + '\n')
        ch = fr.readline()
        ligne += 1

    fw.write("les nombres des mots: " + str(compteur_mots) + '\n')

    fr.close()
    fw.close()
def afficher():
    f = open(nphy3, "r")
    ch = f.readline()
    while(ch != ''):
        print(ch[:len(ch) - 1])
        ch = f.readline()

n = saisie()
remplir()
stocker()
stocker2()
afficher()