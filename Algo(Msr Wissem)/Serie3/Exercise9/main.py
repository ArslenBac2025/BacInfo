from pickle import load, dump

def saisie():
    n = int(input("enter n"))
    return n

n = saisie()

def remplir():
    f = open("nombres.dat", "wb")
    for i in range(n):
        x = int(input("enter x"))
        while(x == 0):
            x = int(input("enter x"))
        dump(x, f)
    f.close()

remplir()

def afficher():
    f = open("nombres.dat", "rb")
    previous_num = load(f)
    EOF = False
    num_change = 0
    while(not(EOF)):
        try:
            curr_num = load(f)
            if(len(str(curr_num)) != len(str(previous_num))):
                num_change+=1
            previous_num = curr_num

        except EOFError:
            EOF = True

    print("it changed " + str(num_change) + " times")

afficher()
