from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque

class MidStack:
    def __init__(self):
        self.upper = ArrayStack()
        self.lower = ArrayDeque()
        
    def is_empty(self):
        return self.upper.is_empty() and self.lower.is_empty()
    
    def __len__(self):
        return len(self.upper) + len(self.lower)
    
    def push(self,elem):
        self.lower.enqueue_last(elem)
        if len(self.upper) < len(self.lower):
            self.upper.push(self.lower.dequeue_first())
    
    def top(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        if self.lower.is_empty():
            return self.upper.top()
        return self.lower.last()
    
    def pop(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        if len(self.upper) > len(self.lower):
            self.lower.enqueue_first(self.upper.pop())
        return self.lower.dequeue_last()
        
    def mid_push(self, elem):
        if len(self.upper) > len(self.lower):
            self.lower.enqueue_first(elem)
        else:
            self.upper.push(elem)