# def count_occurences1(lst,val): #O(n^2)
#     if(not lst): #O(1)
#         return 0
#     else:
#         rest_count = count_occurences1(lst[1:],val) #O(n)
#         if lst[0] == val: #O(1)
#             return 1+rest_count
#         else:
#             return rest_count
# lst = [2,4,5,3,2,3]
# print(count_occurences1(lst,3))
def count_occurences2_user(lst,val):
    x=2
    def count_occurences2(lst,low,high,val): #O(n)
        if(low == high):
            if lst[low] == val:
                return 1
            else:
                return 0
        else:
            rest_count = count_occurences2(lst,low+1,high,val)
            if(lst[low] == val):
                return 1+rest_count
            else:
                return rest_count
    if(len(lst) == 0): #edge case NOT a base case(part of stopping recursive)
        return 0
    return count_occurences2(lst,0,len(lst)-1,val)


lst = [2,4,5,3,2,3]
# print(count_occurences2(lst,0,len(lst)-1,3))
# print(count_occurences2_user(lst,3))


def count_occurences3(lst,val):
    if(not lst):
        return 0
    else:
        last = lst.pop()
        rest_count = count_occurences3(lst,val)
        lst.append(last)
        if last == val:
            return 1+rest_count
        else:
            return rest_count
print(count_occurences3(lst,3))