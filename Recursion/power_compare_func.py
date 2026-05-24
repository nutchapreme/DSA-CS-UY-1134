def power(n):
    if(n==1):
        return a
    else:
        rest = power(a,n-1)
        return rest * a
def not_fast_power(a,n):
    if(n==1):
        return a
    else:
        part1 = not_really_fast_power(a, n//2)
        part2 = not_really_fast_power(a, n//2)
        if(n%2 == 0):
            return part1*part2
        else:
            return a*part1*part2

def fast_power(a,n):
    if(n==1):
        return a
    else:
        part1=fast_power(a,n//2)
        part2 = fast_power(a,n//2)
        if(n%2==0):
            return part1 * part2
        else:
            return a*part1*part2
        
def positive_integers_list(n):
    if(n==1):
        return [1]
    else:
        res = positive_integers_list(n-1) #need to be restored before append
        res.append(n) #
        return res # or positive_integers_list(n-1) + [n]