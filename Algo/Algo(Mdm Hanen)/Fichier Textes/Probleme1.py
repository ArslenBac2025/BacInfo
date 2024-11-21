from numpy import array

mat=array([[str]*100]*100)

def ligne(chtxt):
    l=0
    f=open(chtxt,'r')
    ch=f.readline()
    while(ch!=''):
       l=l+1
       ch=f.readline()
    f.close()
    return l
def colone(chtxt,l):
    f=open(chtxt,'r')
    c=len(f.readline())
    for i in range(l-1):
        if(len(f.readline())>c):
            c=len(f.readline())
    f.close()
    return c - 1

def remplir(mat,l,c):
    f=open(chtxt,'r')
    for i in range(l):
        ch=f.readline()
        ch = ch[:len(ch)-1]
        for j in range(c):
            if(j>=len(ch)):
                mat[i,j]=ord(' ')
            else:
                mat[i,j]=ord(ch[j])
    f.close()

def conv(mat,l,c):
    for i in range(l):
        for j in range(c):
            mat[i,j]=binaire(mat[i,j],8)
            

def binaire(entier, base):
    resultat = ""
    hexo= "0123456789ABCDEF"
    
    while entier > 0:
        rest = entier % base
        if base == 16:
            resultat = hexo[rest] + resultat
        else:
            resultat = str(rest) + resultat 
        entier = entier // base
    
    return resultat

def affich(chtxt1,mat,l,c):
    f=open(chtxt1,'w')
    for j in range(c):
        ch = ''
        for i in range(l):
            print(mat[i,j], end=" ")
            ch += mat[i,j] + " "
        print()
        ch += "\n"
        f.write(ch)
    f.close()



chtxt='txtinit.txt'
chtxt1='txtcrypt.txt'
l=ligne(chtxt)
c=colone(chtxt,l)
remplir(mat,l,c)
conv(mat,l,c)
affich(chtxt1,mat,l,c)