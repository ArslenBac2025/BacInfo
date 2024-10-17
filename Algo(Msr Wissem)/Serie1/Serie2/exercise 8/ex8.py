from numpy import array
from math import sqrt

nphy = "Complexe.txt"

def saisie():
    n = int(input("entrer n \n"))
    while(not(3<=n<=30)):
        n = int(input("entrer n entre 5 and 30 \n"))
    return n
def remplir(nphy):
    f = open(nphy, "w")
    for i in range(n):
        inp = str(input("entre l'equation: " + str(i + 1) + '\n'))
        f.write(inp + '\n')
    f.close()

def Im(ch):
    res = ""
    i = ch.find('i')
    if(i == -1): return 0

    start = i
    while(start != - 1 and ( ch[start] != '+' and ch[start] != '-' and ch[start] != '/' and ch[start] != '*')):
        start -= 1

    start += 1
    end = i

    if(start == end):
        return 1
    else:
        for k in range(start, end):
            res += ch[k]

    return int(res)
def Rel(ch):
    res = ""
    i = 0
    while(i < len(ch) and ch[i] != '+' and ch[i] != '-' and ch[i] != '/' and ch[i] != '*'):
        res += ch[i]
        i+=1

    if(res.find('i') != -1): return 0

    return int(res)

def trier_tab_complex(T, n):
    for i in range(n):
        a = Rel(T[i])
        b = Im(T[i])
        Te[i] = sqrt((a * a) + (b * b))

    for i in range(1,n):
        tempVal = Te[i]
        tempCh = T[i]
        j = i - 1
        while(j >= 0 and Te[j] < tempVal):
            Te[j + 1] = Te[j]
            T[j + 1] = T[j]
            j -= 1
        Te[j + 1] = tempVal
        T[j + 1] = tempCh
def trier(T, n, nphy):
    f = open(nphy,"r")
    i = 0
    ch = f.readline()
    while(ch != ''):
        T[i] = ch[:len(ch)-1]
        ch = f.readline()
        i+=1

    trier_tab_complex(T,n)
    f.close()

    f = open(nphy, "w")
    for i in range(n):
        f.write(T[i] + '\n')
    f.close()

def afficher(nphy):
    f = open(nphy, "r")
    ch = f.readline()
    while(ch != ''):
        print(ch[:len(ch)-1])
        ch = f.readline()
    f.close()


#PROG PRINCIP
n = saisie()
remplir(nphy)

T = array([str]*n)
Te = array([int]*n)

trier(T, n, nphy)
afficher(nphy)