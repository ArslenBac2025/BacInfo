from numpy import array
from pickle import load, dump

tr=array([dict()]*100)
t = array([
    {'lettre': 'I','value': 1},
    {'lettre': 'V','value': 5},
    {'lettre': 'X','value': 10},
    {'lettre': 'L','value': 50},
    {'lettre': 'C','value': 100},
    {'lettre': 'D','value': 500},
    {'lettre': 'M','value': 1000},
])

#programme Python:
def remplir(chtxt):
    f=open(chtxt,'w')
    rep='O'
    n=0
    while(rep=='O'):
        n+=1
        ch=str(input('donner une chaine remain'))
        while(not(len(ch)<50)):
            ch=str(input('donner une chaine remain'))
        f.write(ch+'\n')
        rep=str(input('continuer?')).upper()
        while(not(rep in ['O','N'])):
            rep=str(input('continuer?')).upper()
    return n

def remplir2(chbin,n,chtxt):
    f=open(chbin,'wb')
    ftxt=open(chtxt,'r')
    for i in range(n):
        ch=ftxt.readline()
        ch=ch[:len(ch)-1]
        tr[i]=dict()
        tr[i]['chaine']=ch
        tr[i]['valeur']=result(ch)
        dump(tr[i],f)

def result(ch):
    s = 0
    for i in range(len(ch)):
        num = valeur(ch[i])
        if i < len(ch)-1 and num < valeur(ch[i + 1]):
            s -= num
        else:
            s += num
    return s

def valeur(x):
    for i in range(7):
        if(t[i]['lettre']==x):
            return t[i]['value']

#programme principale:
chtxt='rmain.txt'
chbin='result.dat'
n=remplir(chtxt)
remplir2(chbin,n,chtxt)
