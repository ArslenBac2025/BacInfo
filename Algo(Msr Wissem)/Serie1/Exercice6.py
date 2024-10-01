#imports:
from numpy import*
t=array([dict()]*100)

#Sous-Programmes:
def saisie():
    n=int(input('donner n'))
    while(not(30<=n<=100)):
        n=int(input('donner n'))
    return n

def remplir(t,n):
    for i in range(n):
        t[i]=dict()
        t[i]['nom']=input(f'donner code {i}')
        t[i]['salaire']=float(input(f'donner salaire {i}'))
        t[i]['tache']=input(f'donner tache {i}')
        t[i]['journee']=input(f'donner {i}')
 
def ajouterunEmployer(t,n):
    t[n] = dict()
    t[n]['nom']=input(f'donner code {n}')
    t[n]['salaire']=float(input(f'donner salaire {n}'))
    t[n]['tache']=input(f'donner tache {n}')
    t[n]['journee']=input(f'donner {n}')
    return n+1

def ajouteSalaire(t,n):
    for i in range(n):
        t[i]['salaire']=t[i]['salaire']+1
        
def modifytache(t):
    pos=int(input('donner la position'))
    t[pos]['tache']=input('modify tache')
    print(t[pos])
    
    
    
#Programme Principal:
n=saisie()
remplir(t,n)
ajouterunEmployer(t,n)
modifytache()
ajouteSalaire(t,n)