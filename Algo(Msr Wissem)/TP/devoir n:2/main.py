from random import randint
from pickle import dump, load

def saisie():
    n = int(input("enter n"))
    while not 2 <= n <= 10:
        n = int(input("enter n"))
    return n
def remplir_f(n):

    f = open("MessBrut.txt", "w")
    fb = open("Message.dat", "wb")

    for i in range(n):
        inp = input("enter votre chaine")
        while len(inp) != 26:
            inp = input("enter votre chaine")

        inp = inp.upper()
        encr = ""
        for j in range(26):
            if inp.find(chr(65 + j)) != -1:
                encr += '1'
            else:
                encr += '0'

        f.write(inp + '\n')
        e = dict()
        e["captcha"] = inp
        e["code"] = encr
        dump(e, fb)

        f.write(inp + "\n")

    f.close()
    fb.close()
def afficher():
    f = open("Message.dat", "rb")
    while True:
        try:
            x = load(f)
            print(x["captcha"] + " | " + x["code"] )
        except EOFError:
            break
    f.close()

n = saisie()
mes = ""
remplir_f(n)
afficher()