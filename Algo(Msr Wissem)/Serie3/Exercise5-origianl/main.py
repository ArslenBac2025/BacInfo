from numpy import array
from pickle import load, dump

tr=array([dict()]*100)
my_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


#programme Python:
def remplir(chtxt):
    f=open(chtxt,'w')
    rep='O'
    n=0
    while(rep=='O'):
        n+=1
        ch=str(input('donner une chaine romain'))
        while(not(len(ch)<50)):
            ch=str(input('donner une chaine romain'))
        f.write(ch+'\n')
        rep=str(input('continuer?(O/N)')).upper()
        while(not(rep in ['O','N'])):
            rep=str(input('continuer?(O/N)')).upper()
    f.close()
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
    f.close()
    ftxt.close()

def result(ch):
    s = 0
    for i in range(len(ch)):
        num = my_dict[ch[i]]
        if i < len(ch)-1 and num < my_dict[ch[i + 1]]:
            s -= num
        else:
            s += num
    return s

def afficher():
    f = open(chbin, "rb")
    while True:
        try:
            x = load(f)
            print(x)
        except EOFError:
            break
    f.close()

#programme principale:
chtxt='rmain.txt'
chbin='result.dat'
n=remplir(chtxt)
remplir2(chbin,n,chtxt)
afficher()