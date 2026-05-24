def factorial(n):
    if(n==1):
        return 1
    else:
        rest = factorial(n-1)
        return n*rest
    
    
    