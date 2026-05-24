from DoublyLinkedList import DoublyLinkedList

def copy_linked_list(lnk_lst):
    cp_lst = DoublyLinkedList()
    for data in lnk_lst:
        cp_lst.add_last(data)
    return cp_lst

def deep_copy_linked_list(lnk_lst):
    cp_lst = DoublyLinkedList()
    for data in lnk_lst:
        if isinstance(data,int):
            cp_lst.add_last(data)
        else:
            cp_lst.add_last(deep_copy_linked_list(data))
    return cp_lst 