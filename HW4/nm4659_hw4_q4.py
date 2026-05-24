def list_min(lst,low,high):
    if low == high:
        return lst[low]
    min_val = list_min(lst,low+1,high)
    if lst[low]<min_val:
        return lst[low]
    return min_val


print(list_min([2,3,1,5,7],0,4))
