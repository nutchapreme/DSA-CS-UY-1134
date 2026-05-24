def split_parity(lst):
    left = 0
    right = len(lst) - 1

    while left <= right:
        if (lst[left] % 2 == 0) and (lst[right] % 2 != 0):
            lst[left], lst[right] = lst[right], lst[left]
            right -= 1
            left += 1
        else:
            if lst[right] % 2 == 0:
                right -= 1
            if lst[left] % 2 != 0:
                left += 1
    return lst
