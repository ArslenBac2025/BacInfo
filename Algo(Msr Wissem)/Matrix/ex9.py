from numpy import array

def saisie():
    n = int(input("enter n"))
    while not 2 <= n <= 6:
        n = int(input("enter n"))
    return n

n = saisie()
M = array([[str] * n] * n)

def verif(num):
    cond = True
    i = 0
    while cond and i != len(num):
        if num[i] != '0' and num[i] != '1':
            cond = False
        else:
            i += 1

    return cond

def remplir():
    for i in range(n):
        for j in range(i + 1):
            M[i,j] = str(input("enter nombre bin pour: M[" + str(i) + ',' + str(j) + ']' ))
            while not verif(M[i,j]):
                M[i,j] = str(input("enter nombre bin pour: M[" + str(i) + ',' + str(j) + ']' ))

remplir()

def transfer():
    f = open("files/ex9.txt", "w")
    for i in range(n):
        for j in range(i + 1):
            f.write(M[i,j])
        f.write('\n')
    f.close()

transfer()

def isPalindrome(ch):
    l, r = 0, len(ch) - 1
    cond = True
    while l < r and cond:
        if ch[l] != ch[r]:
            cond = False
        else:
            r -= 1
            l += 1

    return cond

def afficher():
    f = open("files/ex9.txt", "r")
    ch = f.readline()
    while ch != '':
        curr = ch[:len(ch) - 1]
        if isPalindrome(curr):
            print(curr)

        ch = f.readline()
    f.close()


afficher()
