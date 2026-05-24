def split_by_sign(lst,low,high):
    if low >= high:
        return lst
    if lst[low]<0 and lst[high]<0:
        return split_by_sign(lst,low+1,high)
    elif lst[low]>0 and lst[high]>0:
        return split_by_sign(lst,low,high-1)
    elif lst[high]<0 and lst[low]>0:
        lst[low],lst[high]=lst[high],lst[low]
        return split_by_sign(lst,low+1,high-1)
    else: #lst[high]>0 and lst[low]<0
        return split_by_sign(lst, low + 1, high - 1)
