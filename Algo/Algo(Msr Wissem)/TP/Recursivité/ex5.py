def pow(a, n, b, m):
    if(n == 0 and m == 0):
        return 1
    elif(n > 0):
        return a * pow(a, n - 1, b, m)
    else:
        return b * pow(a, n, b, m - 1)
    
print(pow(5, 2, 2, 1))