#imports:
from numpy import*

#Sous-Programmes:
def saisie():
    n=int(input('donner n'))
    while(not(n>10)):
        n=int(input('donner n'))
    return n

def remplir(t,n):
    for i in range(n):
        t[i]=dict()
        t[i]['Cin']=input(f'donner cin {i}')
        t[i]['nom']=input(f'donner nom {i}')
        while(not(len(t[i]['nom'])<=50)):
            t[i]['nom']=input(f'donner nom {i}')
        t[i]['prenom']=input(f'donner prenom {i}')
        while(not(len(t[i]['prenom'])<=50)):
            t[i]['prenom']=input(f'donner nom {i}')
        t[i]['moy1']=float(input(f'donner moy1{i}'))
        t[i]['moy2']=float(input(f'donner moy2 {i}'))
    
def remplirt2(t,t2,n):
    for i in range(n):
        moy1=t[i]['moy1']
        moy2=t[i]['moy2']
        t2[i]['Cin']=t[i]['Cin']
        t2[i]['nom']=t[i]['nom']
        t2[i]['prenom']=t[i]['prenom']
        t2[i]['decision']=input('A ou R')
        t2[i]['moyenne']=(moy1+moy2)/2
        print(t2[i])
        

#Programme Principal:
n=saisie()
t=array([dict()]*n)
t2=array([dict()]*n)
remplir(t,n)
remplirt2(t,t2,n)