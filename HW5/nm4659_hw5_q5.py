from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack
import copy

def permutations(lst):
    stack = ArrayStack()
    collection = ArrayQueue()
    for elem in lst:
        stack.push(elem)
    for i in range(len(stack)):
        new_elem = stack.pop()
        if collection.is_empty():
            collection.enqueue([new_elem])
        else:
            for j in range(len(collection)):
                old = collection.dequeue()
                for k in range(len(old)+1):
                    new = copy.copy(old)
                    new.insert(k,new_elem)
                    collection.enqueue(new)
    return [collection.dequeue() for i in range(len(collection))]

lst=[1,2,3]
print(permutations(lst))