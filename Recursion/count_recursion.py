def count_up(start, end):
    if(start==end):
        print(start)
    else:
        mid = (start+end)//2
        count_up(start,mid)
        count_up(mid+1,end)
        
def count_down(start, end):
    if(start==end):
        print(start)
    else:
        print(end)
        count_down(start,end-1)
        
def count_up_and_down(start, end): #not recommended,use 2 for loop
    if(start==end):
        print(start)
    else:
        print(start)
        count_up_and_down(start+1,end)
        print(start)
        

count_up(1,8)
# count_down(1,8)
#count_up_and_down(1,5)