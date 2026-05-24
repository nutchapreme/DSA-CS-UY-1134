def shift(lst,k,dir = "left"):
    if dir == "left":
        count = 0
        while(count<k):
            val = lst.pop(0)
            lst.append(val)
            count += 1
    elif dir == "right":
        count = 0
        while(count<k):
            val = lst.pop()
            lst.insert(0,val)
            count+=1
    return lst