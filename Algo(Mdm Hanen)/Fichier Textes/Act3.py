from numpy import*

def creer():
    chtxt=input('donner le chemin')
    f=open(chtxt,'w')
    print('1 ajout ')
    print('2 affichage')
    print('3 suppression ')
    print('4 modification ')
    x=int(input('que voulez vous faire'))
    if(x==1):
        ajout(chtxt)
    else if (x==2):
        affich(chtxt)
    else if (x==3):
        supp(chtxt)
    else if(x==4):
        modif(chtxt)

def ajout(chtxt):
    f=open(chtxt,'a')
    ch=input('ajouter quelque chose')
    f.write(ch+'\n')
    f.close()

def affich(chtxt):
    f=open(chtxt,'r')
    ch=f.readline()
    i=1
    while(not(ch=="")):
        print(i+''+ch)
        ch=f.readline()
        i=i+1
    f.close()   
        
def modif(chtxt):
    
    f=open(chtxt,'r')
    ch=f.readline()
    n=0
    t=array([str]*n)
    while(ch!=""):
        t[i]=ch
        ch=f.readline()
        n=n+1
    f.close()
    
    mod=int(input('donner le num de ligne que vous voulez modifiyer'))
    t[mod]=input("entrer le nouvaue phrase")
    t[mod]=t[mod]+'\n'
    f=open(chtxt,'w')
    for i in range(n):
        f.write(t[i])
    f.close()
    
    
def supp(chtxt):
    f=open(chtxt,'r')
    ch=f.readline()
    n=0
    t=array([str]*n)
    while(ch!=""):
        t[i]=ch
        ch=f.readline()
        n=n+1
    f.close()
    
    mod=int(input('donner le num de ligne que vous voulez supprimer'))
    t[mod]=''
    f=open(chtxt,'w')
    for i in range(n):
        if(t[i]!=''):
            f.write(t[i])
    f.close()


#programme principale:
creer()
