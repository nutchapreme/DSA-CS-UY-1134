#even odd without if-else

def even_odd(num):
    res = ["even","odd"]
    return res[num%2]

print(even_odd(2))