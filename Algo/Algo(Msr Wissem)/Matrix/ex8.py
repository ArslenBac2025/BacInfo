from numpy import array
from random import randint

def saisie():
    n = int(input("enter n"))
    while not  2 <= n <= 10:
        n = int(input("enter n"))

    return n

n = saisie()
M = array([[str] * n] * n)

def remplir():
    for i in range(n):
        for j in range(n):
            M[i, j] = chr(randint(65, 90))


remplir()

def afficher():

    print(M)

    for i in range(n):
        ch = ""
        if i == 0 or i == n - 1:
            for j in range(n):
                ch += M[i,j]
            print(ch)

    for j in range(n):
        ch = ""
        for i in range(n):
            ch += M[i][j]
        print(ch)

    ch = ""
    for i in range(n):
        ch += M[i][i]
    print(ch)

    ch = ""
    for i in range(n):
        ch += M[i, n - 1 - i]
    print(ch)


afficher()