f=open('animaux.txt','w')
n=int(input('donner n'))
while(not(2<n<30)):
    n=input('donner n ')
for i in range(n):
    an=input('donner un animal')
    f.write(an+'\n')

f.close()
f=open('animaux.txt','r')
for i in range(n):
    ch=f.readline()
    ch=ch[:len(ch)-1]
    print(ch)