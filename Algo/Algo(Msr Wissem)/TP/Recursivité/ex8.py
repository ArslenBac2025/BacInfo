from numpy import array

t = array([1,2,3,2,1])

def symmetric(t, l, r):
    if(l == r):
        return True
    if(t[l] == t[r]):
        return symmetric(t, l + 1, r - 1)
    else:
        return False 
    
    
print(symmetric(t,0,len(t) - 1))