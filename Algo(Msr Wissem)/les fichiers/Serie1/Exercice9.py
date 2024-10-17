#imports:
from numpy import*

#Sous-Programmes:

def ligne():
    l=int(input('donner L'))
    while(not(3<=l)):
        l=int(input('donner L'))
    return l
    
def colomne():
    c=int(input('donner c'))
    while(not(c<=10)):
        c=int(input('donner c'))
    return c
    
def remplirM(l,c,m):
    for i in range(0,l):
        for j in range(0,c):
            m[i,j]=input('donner une lettre')           
            
def remplirTR(l,c,m):
    global tr
    global a
    tr=array([str]*a)
    a=0
    #verifyer horizontalement
    for i in range(0,l):
        ch=''
        for j in range(0,c):
            ch+=m[i,j]
            if(j==c):
                if(palindrome(ch)):
                    tr[a]=dict()
                    tr[a]['val']=ch
                    tr[a]['num']=print(f'L{i}')
                    a=a+1
                    
    #verifyer vericalement
    pas=0
    while(pas<=c):
        ch=''
        for i in range(0,l):
            ch+=m[i,pas]
            if(i==l):
                if(palindrome(ch)):
                    tr[a]=dict()
                    tr[a]['val']=ch
                    tr[a]['num']=print(f'C{pas}')
                    a=a+1
                pas+=1
    
def palindrome(x):
    x=0
    J=len(x)
    while i<=j:
        if(not(x[i]==x[j])):
            return False
        else:                 
            j=j-1
            x+=1    
    
def AfficherTR(a,tr):
    for i in range(0,a):
        print(t[i])
#Programme Principal:
l=ligne()
c=colomne()
m=array([[str]*l]*c)
remplirM(l,c,m)
remplirTR(l,c,m)
AfficherTR(a,tr)
