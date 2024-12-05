from numpy import array
T = array([1, 2, 3, 4, 5])

def afficher(T, n, i):
    if(not(i >= n)):
        print(T[i])
        return afficher(T, n, i + 1)
    
afficher(T, 5, 0)