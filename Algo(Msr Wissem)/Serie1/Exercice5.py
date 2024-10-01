#imports:
from numpy import*

#Sous-Programmes:

def saisie():
    n=int(input('donner nembre des films'))
    while(not(n>10)):
        n=int(input('donner nembre des films'))
    return n

def remplir(t):
    for i in range(n):
        t[i]=dict()
        t[i]['code']=int(input(f'donner code du film{i}'))
        t[i]['nom']=input(f'donner nom du film{i}')
        t[i]['acteurP']=input(f'donner acteur p du film{i}')
        t[i]['annee']=input(f'donner anne du film{i}')
            
def NFilm2006(t,n):
    s=0
    for i in range(n):
        if t[i]['annee']==2006:
            s=s+1
    return s

def Affichage(t,n):
    for i in range(n):
        if (t[i]['acteurP']=='Brad Pit'):
            print(t[i]['nom'])
            print(t[i]['code'])
    
    
#Programme Principal:
n=saisie()
t=array([dict()]*n)
remplir(t)
NFilm2006(t,n)
Affichage(t,n)