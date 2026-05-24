def remove_consecutive(lst,low,high):
    if low>=high:
        return [lst[high]]
    res = remove_consecutive(lst,low,high-1)
    if lst[high]==lst[high-1]:
        high-=1
    else:
        res.append(lst[high])
    return res

lst=[1,1,3,4,4,4,5]
print(remove_consecutive(lst,0,6))