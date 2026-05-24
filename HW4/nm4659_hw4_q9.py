def permutations(lst, low, high):
    if low == high:
        return [[lst[low]]]
    res = []
    for i in range(high - low + 1):
        for s in permutations(lst, low + 1, high):
            s.insert(i, lst[low])
            res.append(s)
    return res
