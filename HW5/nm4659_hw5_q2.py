from ArrayStack import ArrayStack

class MaxStack:
    def __init__(self):
        self.stack = ArrayStack()
        self.maximum = None
        
    def is_empty(self):
        return self.stack.is_empty()
    
    def __len__(self):
        return len(self.stack)
    
    def push(self,elem):
        self.stack.push((elem, self.maximum))
        if self.maximum is None or elem > self.maximum:
            self.maximum = elem
    
    def top(self):
        if self.is_empty():
            raise Exception("MaxStack is empty")
        return self.stack.top()[0]
    
    def pop(self):
        if self.is_empty():
            raise Exception("MaxStack is empty")
        res = self.stack.pop()
        self.maximum = res[1]
        return res[0]
        
    def max(self):
        if self.is_empty():
            raise Exception("MaxStack is empty")
        return self.maximum