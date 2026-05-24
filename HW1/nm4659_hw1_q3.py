def sum_sqr(n):
    sum = 0
    for i in range(n):
        sum += i*i
    return sum

sum([i*i for i in range(n)])

def sum_sqr_odd(n):
    sum = 0
    for i in range(1,n,2):
        sum += i*i
    return sum

sum([i*i for i in range(1,n,2)])
