from numpy import*

t=array([dict()]*100)

def saisie():
    n=int(input('donner n'))
    while(not(n>20)):
        n=int(input('donner n'))
    return n

def remplir(n,t):
    for i in range(n):
        t[i]=dict()
        
        t[i]['num']=int(input('donner num'))
        while(not(1000<=t[i]['num']<=9999)):
            print('de 4 chiffre!!!')
            t[i]['num']=int(input('donner num'))
        
        t[i]['np']=input('doinner np')
        while(not(len(t[i]['np'])>=30)):
            print('de 30 caractere!!!')
            t[i]['np']=input('doinner np')
        
        t[i]['dn']=input('doinner dn')
        while(not(len(t[i]['np'])>=10)):
            print('de 10 caractere!!!')
            t[i]['dn']=input('doinner np')
        
        t[i]['cl_el']=dict()
        t[i]['cl_el']['nom_cl']=input('donner nom cl')
        while(not(verif(t[i]['cl_el']['nom_cl']))):
            t[i]['cl_el']['nom_cl']=input('donner nom cl')
        t[i]['cl_el']['num_cl']=int(input('donner num cl'))
        t[i]['cl_el']['moyen']=float(input('donner moyenne'))
        
def verif(ch):
    return ch[0]=4 and (ch[1:]='SI' or ch[1:]='MA' or ch[1:]='SE' or ch[1:]='TE' or ch[1:]='EG' or ch[1:]='LE' )
        
def affiche(chtxt,n,t):
    f=open(chtxt,'w')
    s=0
    ind=0
    ind2=0
    mm=t[ind]['cl_el']['moyen']
    mms=t[ind2]['cl_el']['moyen']
    
    for i in range(n):
        if(t[i]['cl_el']['moyen']>=10):
            s=s+1
        if(i>0):
            if(t[i]['cl_el']['moyen']>mm):
                ind=i
            if(t[i]['cl_el']['nom_cl'][2:]=='SI' and t[i]['cl_el']['moyen']>mms):
                ind2=i
            
    f.write('nb eleve:'+str(n)+''+'nb moyen > 10 '+str(s)+'\n')
    f.write(t[ind]['np']+'a le meilleur note'+'\n')
    f.write(t[ind2]['np']+'a le meilleur note dans le classe SI'+'\n')
    f.close()
    

#programme principale:
n=saisie()
remplir(n,t)
chtxt='statistique.txt'
affiche(chtxt,n,t)
    

