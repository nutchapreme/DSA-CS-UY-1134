def fibs(n):
    first = 1
    second = 1
    for i in range(n):
        sum = first + second
        yield first
        first = second
        second = sum