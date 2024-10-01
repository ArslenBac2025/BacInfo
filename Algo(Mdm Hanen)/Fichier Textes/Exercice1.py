from numpy import*
t=array([str]*100)

def saisie(chtxt):
    f.open(chtxt,'w')
    n=0
    ch=input('donner une chaine')
    while(not(verif(ch))):
        ch=input('donner une chaine')
    f.write(ch+'\n')
    des=input('voulez vous continue	? o/n : ')
    while(des==o):
        n=n+1
        ch=input('donner une chaine')
        while(not(verif(ch))):
            ch=input('donner une chaine')
        f.write(ch+'\n')
        des=input('voulez vous continue	? o/n : ')
    f.close()
    return n

def remplir(chtxt,n,t):
    f=open(chtxt,'r')
    for i in range(n):
        t[i]=dict()
        t[i]['nl']=i
        t[i]['nbm']=nbm(f.readline())
    f.close()
    
    
def nbm(ch):
    ch=ch[:len(ch)-1]
    s=0
    for i in range(len(ch)):
        if(ch[i]==' ' ):
            s=s+1
    return s+1    
    
def afficher(t,n):
    for i in range(n):
        print(t[i]['nl'])
        print(t[i]['nbm'])

chtxt='fichier.txt'
n=saisie(chtxt)
remplir(chtxt,n,t)
afficher(t,n)

