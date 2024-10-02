def remplir(chtxt):
    f=open(chtxt,'w')
    n=0
    rep='O'
    while(rep=='O'):
        ch=input('donner une operation')
        f.write(ch+'\n')
        n+=1
        rep=input('autre operation? O/N: ').upper()
    f.close()
    return n 
        

def resultat(chtxt1,n):
    f=open(chtxt,'r')
    f1=open(chtxt1,'w')
    for i in range(n):
        ch=f.readline()
        ch=ch[0:len(ch)-1]
        f1.write(ch+str(result(ch))+'\n')
    f.close()
    f1.close()
    
        
    
def result(ch):
    s = 0
    num = 0
    op = '+'
    
    for i in range(len(ch)):
        if '0'<ch[i]<'9':
            num = num * 10 + int(ch[i]) 
        elif ch[i] in ['+', '-', '*', '/', '=']:
            if op == '+':
                s += num
            elif op == '-':
                s -= num
            elif op == '*':
                s *= num
            elif op == '/':
                s //= num
            op = ch[i]  
            num = 0  
    
    return s

chtxt='calcul.txt'
chtxt1='resultat.txt'
n=remplir(chtxt)
resultat(chtxt1,n)
            
        
