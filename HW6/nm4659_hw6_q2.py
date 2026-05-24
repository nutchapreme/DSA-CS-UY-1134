from DoublyLinkedList import DoublyLinkedList

class Integer:
    def __init__(self, num_str):
        self.digit = DoublyLinkedList()
        for i in num_str:
            self.digit.add_last(int(i))
        
    def __add__(self, other):
        res = Integer("")
        cursor1 = self.digit.trailer.prev
        cursor2 = other.digit.trailer.prev
        carry = 0
        while not((cursor1.data is None) and (cursor2.data is None)):
            if cursor1.data is not None:
                left = cursor1.data
                cursor1 = cursor1.prev
            else:
                left = 0
                
            if cursor2.data is not None:
                right = cursor2.data
                cursor2 = cursor2.prev
            else:
                right = 0

            val = left + right + carry
            carry = val//10
            next_digit = val%10
            res.digit.add_first(next_digit)
        if carry == 1:
            res.digit.add_first(carry)
            
        return res
        
    def __repr__(self):
        switch = False
        res = []
        for i in self.digit:
            if i != 0:
                switch = True
            if switch:
                res.append(str(i))
        if switch is False:
            return "0"
        return "".join(res)
    
    def __mul__(self, other):
        
    
    def __mul__(self, other):
        res = Integer("")
        cursor1 = self.digit.trailer.prev
        shift = 0
        while cursor1 != self.digit.header:
            carry = 0
            left = cursor1.data
            store = Integer("")
            for i in range(shift):
                store.digit.add_last(0)
            cursor2 = other.digit.trailer.prev
            while cursor2 != other.digit.header:
                right = cursor2.data
                val = (left * right) + carry
                carry = val//10
                next_digit = val%10
                store.digit.add_first(next_digit)
                cursor2 = cursor2.prev
            if carry > 0:
                store.digit.add_first(carry)

            res = res+store
            cursor1 = cursor1.prev
            shift+=1
                
        while res.digit.header.next.data == 0 and len(res.digit)>1:
            res.digit.delete_first()
            
        return res
a = Integer("346")
b = Integer("12")
print(a*b)
        