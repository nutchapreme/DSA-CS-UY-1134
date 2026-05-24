#1
def simple_power(a,n):
    if n==0:
        return 1
    else:
        return a*simple_power(a,n-1)

print(simple_power(3,3))

#2
def power_tree(a,n):
    if n==1:
        return a
    if n==0:
        return 1
    else:
        first = power_tree(a,n//2)
        second = power_tree(a,n//2)
        if n%2==0:
            return first*second
        return a*first*second
print(power_tree(3,3))

def reverse_integers_list(n): #FIX
    if len(n)==0:
        return []
    else:
        res = reverse_integers_list(n[1:])
        res.append(n[0])
        return res

lst=[1,2,9,0,3,4]
print(reverse_integers_list(lst))

#4
def sum_of_powers(a,n): 
    if n==1:
        return a
    else:
        return a**n + sum_of_powers(a,n-1)
    
print(sum_of_powers(1,3))

#6
def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)

print(factorial(4))

#7
def even_numbers_list(n):
    if n<2 or n%2==1:
        return []
    return even_numbers_list(n-2) + [n]
print(even_numbers_list(6))

