from numpy import array

t = array([1,2,3])

def somme(T, n, i):
    if(i >= n):
        return 0
    return T[i] + somme(T, n, i + 1)

print(somme(t, len(t), 0))