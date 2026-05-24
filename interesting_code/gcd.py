def gcd(numerator, denominator): #euclidean
    if denominator == 0:
        raise ZeroDivisionError("can't divide by zero!")
    if numerator == denominator:
        return numerator
    if denominator>numerator:
        r = denominator-(numerator*(denominator//numerator))
        left = numerator
        right = denominator
    if numerator>denominator:
        r = numerator-(denominator*(numerator//denominator))
        left = denominator
        right = numerator
    while right>0:
        r=left-(right*(left//right))
        left = right
        right = r
        if right == 0:
            return left
    return 1

def simplify_frac(numerator,denominator):
    divide = gcd(numerator,denominator)
    numerator//=divide
    denominator//=divide
    return str(numerator)+"/"+str(denominator)


print(gcd(81, 27))
print(simplify_frac(81,27))