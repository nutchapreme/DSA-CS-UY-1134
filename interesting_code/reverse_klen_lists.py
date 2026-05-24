def reverse_klen_lists(lst,k):
    low = 0
    high = k-1
    while low<=high and high <= len(lst)-1:
        lst[low],lst[high]=lst[high],lst[low]
        low+=1
        high-=1
        if low==high:
            low+=(k//2)+1
            high+=(3*k)//2
    return lst
lst = [-5,3,-2,7,-1,6,4,7,8,3]
print(func(lst,3))