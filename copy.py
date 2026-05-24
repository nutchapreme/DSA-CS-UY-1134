import copy
def func(lst):
    lst1 = copy.copy(lst)
    lst2 = copy.deepcopy(lst)
    lst[0] = 11
    lst1[1][1] = 33
    lst2[2] = [44, 55]
    print("Inside func: lst = ",lst)
    print("Inside func: lstl =",lst1)
    print("Inside func: lst2 =", lst2)
data = [10, [20, 30], [40, 50]]
func(data)
print("Outside: data = ", data) #list mutable



