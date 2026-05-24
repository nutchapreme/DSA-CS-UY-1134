def remove_all(lst,value):
    left = 0
    right = 1
    if (not lst) or (len(lst)==1 and lst[0] != value):
        return lst
    if len(lst)==1 and lst[0] == value:
        return []
    print(lst)
    while right<=len(lst)-1:
        if lst[left] == value:
            if lst[right] != value:
                lst[left],lst[right] = lst[right],lst[left]
        if lst[left]!=value:
            left+=1
        right+=1
    count = len(lst)-left
    for i in range(count):
        lst.pop()
    return lst


lst=[1]
print(remove_all(lst,1))