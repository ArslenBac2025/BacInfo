from ftplib import print_line
from numpy import array

chemin = "TxtInit.txt"

def plus_long():
    max = 0
    f = open(chemin, "r")

    ch = f.readline()
    while(ch != ''):
        if(len(ch[:len(ch) - 1]) > max):
            max = len(ch) - 1
        ch = f.readline()

    f.close()

    return max
C = plus_long()
L = 0
M = array([[int] * 50] * C)

def remplir(L, C):
    f = open(chemin, "r")

    i = 0
    ch = f.readline()

    while(ch):
        L += 1
        ch = ch[:len(ch) - 1]
        for j in range(C):
            if(j > len(ch) - 1):
                M[i,j] = 32
            else :
                M[i,j] = ord(ch[j])
        ch = f.readline()
        i+= 1

    f.close()
    return L

L = remplir(L,C)

def convert_huit(num):
    temp = ""
    added_char = ''
    while(num):
        added_char = str(num % 8)
        num = num // 8
        temp += added_char

    res = ""
    for i in range(len(temp) - 1, -1, -1):
        res += temp[i]

    return int(res)
def convertir_mat(L,C):
    for i in range(L):
        for j in range(C):
            M[i,j] = convert_huit(M[i,j])
convertir_mat(L,C)

def afficher():
    for j in range(0, C):
        for i in range(0, L):
            print(M[i, j], end = " ")
        print()
afficher()