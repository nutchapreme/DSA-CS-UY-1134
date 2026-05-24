def e_approx(n):
    sum = 1.0
    factorial = 1
    for i in range(1,n+1):
        factorial*=i
        sum += 1/factorial
        
    return sum