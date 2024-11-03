from numpy import array

def verif(ch):
    #longeur
    cond = False
    if not 5 <= len(ch) <= 10: return cond

    #majuscule
    i = 0
    cond = True
    while cond and i < len(ch):
        if not ('A' <= ch[i] <= 'Z'):
            cond = False
        else:
            i+=1

    #distincts
    temp = ch
    while len(temp) != 0 and cond:
        car = temp[0]
        temp = temp[1::]
        i = 0
        while i < len(temp) and cond:
            if temp[i] == car:
                cond = False
            else:
                i += 1

    return cond

def saisie():
    key = str(input("give key for encrypting \n"))
    while not verif(key):
        key = str(input("give key for encrypting \n"))

    return key

def operation(ch, key):
    spaces = 0
    cols = len(key)
    rows = len(ch)
    while rows % len(key) != 0:
        rows += 1
        spaces += 1

    rows //= cols

    M = array([[str] * cols] * rows)

    k = 0
    for i in range(rows):
        for j in range(cols):
            if k >= len(ch):
                M[i,j] = ' '
            else:
                M[i,j] = ch[k]
                k += 1

    chcryp = ""
    for i in range(cols):
        chcryp += key[i]
        for j in range(rows):
            chcryp += M[j,i]

    return chcryp[:len(chcryp) - spaces]

def crypter():
    fr = open("files/source.txt", "r")
    fw = open("files/crypt.txt", "w")
    ch = fr.readline()
    while ch != '':
        text = ch[:-1]
        chcryp = operation(text, key)
        fw.write(chcryp + '\n')
        ch = fr.readline()

    fr.close()
    fw.close()

def afficher():
    f = open("files/crypt.txt", "r")
    ch = f.readline()
    while ch:
        print(ch[:-1])
        ch = f.readline()

    f.close()

key = saisie()
crypter()
afficher()



