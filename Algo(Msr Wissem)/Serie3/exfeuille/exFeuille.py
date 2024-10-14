from numpy import array
from pickle import dump,load



#programme Python:

def saisie():
    n=int(input('donner ne'))
    while(not(3<=n<=20)):
        n=int(input('donner ne'))
    return n

def remplir(n,chbin):
    f=open(chbin,'wb')
    for i in range(n):
        e=dict()
        e['np']=str(input('donner np'))
        while(not(verif1(e['np']))):
            e['np']=str(input('donner np'))
        e['moy']=float(input('donner moy'))
        e['cin']=input('donner cin')
        while(not(verif2(e['cin']))):
            print('le cin doit etre former par 8 chiffres')
            e['cin']=input('donner cin')
        print(e['cin'])
        dump(e, f)
    f.close()

def verif1(ch):
    count=0
    for i in range(len(ch)):
        if ch[i]==' ':
            count+=1
    if(count!=1):
        return False
    else:
        for i in range(len(ch)):
            if(ch[i]!=' '):
                if(not('A'<=ch[i].upper()<='Z')):
                    return False

def verif2(x):
    x=str(x)
    return len(x)==8

def affichage(n,chadmin,chrefuse,chbin):
    f1=open(chbin,'rb')
    f2=open(chadmin,'wb')
    f3=open(chrefuse,'w')
    for i in range(n):
        eleve = load(f1)
        if(eleve["moy"]>=10):
            dump(eleve, f2)
        elif (eleve["moy"]<10):
            f3.write(eleve['np']+'\n')
            



#programme principale:
chbin='eleve.bin'
chadmi='admi.bin'
chrefuse='refuser.txt'
n=saisie()
remplir(n,chbin)
affichage(n,chadmi,chrefuse,chbin)
