from pickle import load, dump
from random import randint
from numpy import array

def saisie():
    global n
    n = int(input("enter n"))
    while not 3 <= n <= 15:
        n = int(input("enter n"))
def remplir():
    f = open("nombres.dat", "wb")
    for i in range(n):
        dump(randint(0, 1000), f)
    f.close()
def remplir_t(tab, dict_chiff, e, n):

    for i in range(0,10):
        dict_chiff[i] = 0

    f = open("nombres.dat", "rb")
    for i in range(n):
        l = load(f)
        string = str(l)
        for c in range(len(str(l))):
            dict_chiff[int(string[c])] += 1

    f.close()

    for i in range(0, 10):
        e = dict()
        e["num"] = i
        e["val"] = dict_chiff[i]
        tab[i] = e

    max = 0
    for i in range(1, n):
        if tab[max]["val"] < tab[i]["val"]:
            max = i

    min = 0
    for i in range(1, n):
        if tab[min]["val"] > tab[i]["val"]:
            min = i

    print("le nombre porte bonheur est: " + str(tab[max]["num"]) + str(tab[min]["num"]))


def afficher():
    #amaltha al jaou
    f = open("nombres.dat", "rb")
    while True:
        try:
            x = load(f)
            print(x)
        except EOFError:
            break

n = 0
saisie()
remplir()

dict_chiff = dict()
e = dict(num = int(), val = int())
tab = array([e] * 10)

remplir_t(tab, dict_chiff, e, n)
afficher()