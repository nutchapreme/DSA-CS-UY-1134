def is_sorted(lst,low,high):
    if low == high:
        return True
    if lst[high]>=lst[high-1]:
        return is_sorted(lst,low,high-1)
    return False

lst = [-2,2,3,4,7]
print(is_sorted(lst,0,4))