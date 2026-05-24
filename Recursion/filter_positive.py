def filter_positive(lst,low,high):
    if low==high:
        if lst[low]>=0:
            return [lst[low]]
        return []
    if lst[low]<0:
        return filter_positive(lst,low+1,high)
    if lst[low]>=0:
        return [lst[low]]+filter_positive(lst,low+1,high)


def filter_positive1(lst,low,high):
    if low==high:
        if lst[low]>=0:
            return [lst[low]]
        return []
    prev = filter_positive1(lst,low+1,high)
    if lst[low]>0:
        prev.append(lst[low])
    return prev


        
lst = [1,-2,4,1,5,-4,-1,0,9]
print(filter_positive(lst,0,8))
print(filter_positive1(lst,0,8))