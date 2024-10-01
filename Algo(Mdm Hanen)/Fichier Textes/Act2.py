f=open('D:\original.txt','r')
ff=open('copie.txt','w')

ch=f.readline()
i=1
while(not(ch="")):
    ff.write(i+' '+ch)
    ch=f.readline()
    i=i+1