def two_sum(srt_lst, target):
    sum = 0
    i = 0
    j = len(srt_lst)-1
    while i<j:
        if srt_lst[i] + srt_lst[j] == target:
            return (i,j)
        else:
            if srt_lst[i]+srt_lst[j]<target:
                i+=1
            if srt_lst[i]+srt_lst[j]>target:
                j-=1
    return None
            