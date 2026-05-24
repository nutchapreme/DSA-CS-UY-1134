from DoublyLinkedList import DoublyLinkedList

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    def merge_sublists(node1, node2):
        if node1.data is None and node2.data is None:
            return DoublyLinkedList()
        if node1.data is None:
            res = merge_sublists(node1, node2.next)
            res.add_first(node2.data)
            return res
        if node2.data is None:
            res = merge_sublists(node1.next, node2)
            res.add_first(node1.data)
            return res
        
        if node1.data <= node2.data:
            res = merge_sublists(node1.next, node2)
            res.add_first(node1.data)
            return res
        else:
            res = merge_sublists(node1, node2.next)
            res.add_first(node2.data)
            return res
    return merge_sublists(srt_lnk_lst1.header.next, srt_lnk_lst2.header.next)