def findChange(lst01):
    left = 0
    right = len(lst01)-1
    if lst01[0]==1:
        return 0
    while left<=right:
        mid = (left+right)//2
        if lst01[mid] == 1 and (mid==0 or lst01[mid-1] == 0):
            return mid
        elif lst01[mid] == 1:
            right = mid-1
        else:
            left = mid+1
    return None


lst01=[0,0,0]
print(findChange(lst01))
