from DoublyLinkedList import DoublyLinkedList
class CompactString:
    def __init__(self, orig_str):
        self.data = DoublyLinkedList()
        if not orig_str:
            return
        count = 1
        for i in range(1,len(orig_str)):
            if orig_str[i] == orig_str[i-1]:
                count+=1
            else:
                self.data.add_last((orig_str[i-1],count))
                count = 1
        self.data.add_last((orig_str[-1],count))
    def __add__(self, other):
        res = CompactString("")
        cursor = self.data.header.next
 
        while cursor!=self.data.trailer:
            res.data.add_last(cursor.data)
            cursor = cursor.next
        if self.data.trailer.prev.data[0] == other.data.header.next.data[0]:
            merged_char = self.data.trailer.prev.data[0]
            merged_count = self.data.trailer.prev.data[1] + other.data.header.next.data[1]
            
            res.data.delete_last()
            res.data.add_last((merged_char, merged_count))
            other_cursor = other.data.header.next.next
        else:
            other_cursor = other.data.header.next
            
        while other_cursor != other.data.trailer:
            res.data.add_last(other_cursor.data)
            other_cursor = other_cursor.next
            
        return res
    
    def __lt__(self, other):
        return repr(self)<repr(other)
    def __le__(self, other):
        return repr(self)<=repr(other)
    def __gt__(self, other):
        return repr(self)>repr(other)
    def __ge__(self, other):
        return repr(self)>=repr(other)
    def __repr__(self):
        cursor = self.data.header.next
        res = ""
        while cursor != self.data.trailer:
            res += cursor.data[0] * cursor.data[1]
            cursor = cursor.next
        return res
    