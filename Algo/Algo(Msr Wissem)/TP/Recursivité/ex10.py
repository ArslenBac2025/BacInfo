from numpy import array
t = array([0] * 5)

def remplir(t, i, n):
    if(i == n):
        print(t)
    else:
        t[i] = int(input("entrer column: " + str(i) + '\n'))
        while(not (t[i] > 0)):
            t[i] = int(input("entrer column: " + str(i) + '\n'))            
        return remplir(t, i + 1, n)
    
remplir(t, 0, 5)