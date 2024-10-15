from pickle import dump, load
from numpy import array
import os

f = dict()
T = array([f] * 100)

nphy = "club.dat"
n = 0


def ajouter():
    F = open(nphy, "ab")
    f = dict()
    f["nom"] = str(input("enter nom du film"))
    f["acteur"] = str(input("entrer nom d'acteur"))
    f["num_copie"] = int(input("entrer nombre des copies"))
    dump(f, F)
    f = dict()
    print("success!")
    F.close()
def supprimer():
    F = open(nphy, "rb")
    n = 0
    while True:
        try:
            T[n] = load(F)
            n+=1
        except EOFError:
            break

    F.close()

    i = 0
    F = open(nphy, "wb")
    while(i < n):
        if(T[i]["num_copie"] != 1):
            dump(T[i], F)
            i+=1
        else:
            i+=1
    F.close()
def afficher_par_acteur():
    F = open(nphy, "rb")
    nom_acteur = str(input("entrer nom d'acteur"))
    while True:
        try:
            ft = load(F)
            if(ft["acteur"] == nom_acteur):
                print(ft)
        except EOFError:
            break
    F.close()
def trier_films():
    F = open(nphy, "rb")
    i = 0
    while True:
        try:
            T[i] = load(F)
            i+=1
        except EOFError:
            break

    n = i
    isSorted = False
    while(not(isSorted)):
        isSorted = True
        for i in range(1, n):
            if(T[i - 1]["nom"] > T[i]["nom"]):
                temp = T[i - 1]
                T[i - 1] = T[i]
                T[i] = temp
                isSorted = False

    for i in range(n):
        print(T[i]["nom"])


def afficher():
    F = open(nphy, "rb")
    while True:
        try:
            x = load(F)
            print(x)
        except EOFError:
            break
def run():
    choix = ""
    while(choix != "EXIT"):
        choix = str(input("enter votre choix:\n"
                          "1- ajouter un film\n"
                          "2- supprimer les fims avec une seule copie\n"
                          "3- afficher le film d'un acteur\n"
                          "4- trier les film alphabetiquement\n"
                          "EXIT- echapper le program\n"))
        if(choix == "1"):
            ajouter()
        if(choix == "2"):
            supprimer()
        if(choix == "3"):
            afficher_par_acteur()
        if(choix == "4"):
            trier_films()

        if(choix != "EXIT" and choix != '3' and choix != '4'):
            afficher()

        if(choix != "EXIT"):
            str(input("press any key to continue"))
            #this was done so I could create some spacing
            for i in range(10):
                print('\n')

    print("programme a été terminé avec succèss")

run()