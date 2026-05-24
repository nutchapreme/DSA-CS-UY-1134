def appearances(s,low,high):
    res={}
    if low == high:
        res[s[low]]=1
        return res
    res = appearances(s,low+1,high)
    if s[low] not in res:
        res[s[low]]=1
    else:
        res[s[low]]+=1
    return res


    
    