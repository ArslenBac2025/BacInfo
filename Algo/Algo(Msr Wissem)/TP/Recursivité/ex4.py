def pow(a, n):
    if n == 0:
        return 1
    return a * pow(a, n - 1)
    
print(pow(5, 2))