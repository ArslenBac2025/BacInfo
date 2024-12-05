from numpy import array

t = array([1, 2, 3, 4, 5, 6])

def reverse(T, i, n):
    if(i == n // 2):
        print(T)
    else:        
        T[i], T[n - 1 - i] = T[n - 1 - i], T[i]
        return reverse(T, i + 1, n)

reverse(t, 0, 6)
