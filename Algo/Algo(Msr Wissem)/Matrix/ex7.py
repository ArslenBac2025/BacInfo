from numpy import array
from random import randint

def saisie():
    n = int(input("enter n \n"))
    while not 2 <= n <= 10:
        n = int(input("entrer n \n"))

    return n


def remplir():
    for i in range(n):
        for j in range(n):
            M[i,j] = randint(100, 999)

def trouver():
    to_find = int(input("enter number to find \n"))
    counter = 0
    for i in range(n):
        for j in range(n):
            num = str(M[i,j])
            for k in range(len(num)):
                if num[k] == str(to_find):
                    counter += 1
    return counter

def afficher():
    for i in range(n):
        for j in range(n):
            print(M[i,j], end = " ")
        print()

    how_much = trouver()
    print("the number you entered repeats: " + how_much)

n = saisie()
M = array([[0] * n] * n)
remplir()
afficher()
