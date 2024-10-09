nphy1 = "commande.txt"
nphy2 = "facture.txt"


def verif(ch):
    computer_espace = 2
    code_article = ch[:4]
    cond = False
    if(code_article.isnumeric() == False): return cond

    i = 4
    quantite = ""
    prix = ""
    while(i < len(ch)):
        if(ch[i] == ' '):
            computer_espace-=1
            i+=1
        if(computer_espace == 1):
            quantite += ch[i]
        elif(computer_espace == 0):
            prix += ch[i]
        i+=1

    if(quantite.isnumeric() == False or prix.isnumeric() == False): return cond

    cond = True
    return cond
def remplir():
    f = open(nphy1, "w")
    writeMode = True
    while(writeMode):
        string = str(input(">"))
        while(verif(string) == False):
            string = str(input(">"))
        f.write(string + '\n')
        choice = str(input("arreter?(O/n)"))
        while(choice.upper != 'O' and choice.upper() == 'N'):
            choice = str(input("arreter?(O/n)"))
        if(choice.upper() == 'O'):
            writeMode = False
    f.close()


def calculer(ch):
    id = ch[:4]
    i = 4
    computer_espace = 2
    quantite = ""
    prix = ""

    while(i < len(ch)):
        if(ch[i] == ' '):
            computer_espace-=1
            i+=1
        if(computer_espace == 1):
            quantite += ch[i]
        elif(computer_espace == 0):
            prix += ch[i]
        i+=1
    nvch = str(id) + ' ' + str(int(quantite) * int(prix))
    return nvch
def stocker():
    fr = open(nphy1,"r")
    fw = open(nphy2, "w")

    ch = fr.readline()
    while(ch != ''):
        nvtext = calculer(ch[:len(ch) - 1])
        fw.write(nvtext + '\n')
        ch = fr.readline()

    fr.close()
    fw.close()

def afficher():
    f = open(nphy2, "r")
    ch = f.readline()
    while(ch != ''):
        print(ch[:len(ch) - 1])
        ch = f.readline()

    f.close()

remplir()
stocker()
afficher()