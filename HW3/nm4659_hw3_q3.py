def find_duplicates(lst):
    duplicate = []
    counter = [0]*(len(lst)-1)
    
    for index in range(len(lst)):
        counter[lst[index]-1] += 1
    for index in range(len(counter)):
        if counter[index] > 1:
            duplicate.append(index+1)
    return duplicate
    
lst = [1,1,2,2,1]
print(find_duplicates(lst))