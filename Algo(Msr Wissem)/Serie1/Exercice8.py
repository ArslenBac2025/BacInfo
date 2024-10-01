#imports:
from numpy import
t=array([dict()]*30)

#Sous-Programmes:
def saisie():
    n=int(input('donner n'))
    while(not(5<=n<=30)):
        n=int(input('donner n'))
    return n

def remplir(t,n):
    #ma 3maltech verificationet 5tr na3rafhom "B5ilt 3lehom"
    for i in range(n):
        t[i]=dict()
        t[i]['Dat-Emi']=dict()
        t[i]['Code']=input(f'donner code {i}')
        t[i]['Auteur']=input(f'donner Auteur {i}')
        t[i]['Dat-Emi']['j']=input(f'donner jour {i}')
        t[i]['Dat-Emi']['m']=input(f'donner month {i}')
        t[i]['Dat-Emi']['a']=input(f'donner annee {i}')
        t[i]['titre']=input(f'donner titre {i}')
        t[i]['prix']=input(f'donner prix {i}')
        
def affichage(t,n):
    moyenne=0
    
    print('les code des livre dont prix>10')
    for i in range(n):
        if(t[i]['prix']>10):
            print(t[i]['Code'])
        moyenne=moyenne+t[i]['prix']
        
    print('moyenne')
    print(moyenne/n)
    
    print('Les auteurs des livres les plus cheres')
    for i in range(n):
        if(t[i]['prix']>moyenne):
            print(t[i]['Auteur'])
            
    code=int(input('donner le code'))
    for i in range(n):
        if(t[i]['code']==code):
            print(t[i])
        else:
            print('livre inexistant')
    
def modifyPrix(t,n):
    index=int(input('donner posiiton'))
    for i in range(n):
        if(i==index):
            t[i]['prix']=int(input('donner nouveau prix'))
            
def triage(t,n):
    p=0
    element=t[p]
    for i in range(1,n):
        if(element['prix']>t[i]['prix']):
            element,t[i]=t[i],element
        p=p+1
    print(t)
        
    
#Programme Principal:
n=saisie()
remplir(t,n)
affichage1(t,n)
modifyPrix(t,n)
triage(t,n)