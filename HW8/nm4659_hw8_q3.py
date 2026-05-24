from BinarySearchTreeMap import BinarySearchTreeMap

def restore_bst(prefix_lst):
    bst = BinarySearchTreeMap()
    if len(prefix_lst)==0:
        return bst
    min_val = min(prefix_lst)-1
    def restore_subtree(min_val,max_val,i):
        if i >= len(prefix_lst):
            return None, i
        curr_key = prefix_lst[i]
        if not (min_val<curr_key<max_val):
            return None, i

        item = bst.Item(curr_key)
        curr_node = bst.Node(item)
        i+=1
        
        curr_node.left, i = restore_subtree(min_val, curr_key, i)
        if curr_node.left:
            curr_node.left.parent = curr_node
        
        curr_node.right, i = restore_subtree(curr_key, max_val, i)
        if curr_node.right:
            curr_node.right.parent = curr_node
            
        return curr_node, i
    low = min(prefix_lst)-1
    high = max(prefix_lst)+1
    bst.root, index = restore_subtree(low,high,0)
    bst.n = len(prefix_lst)
    return bst
        
        
        
        
        
                           
                           
                           
    
    
    
    bst.root = restore_subtree(float(-inf),float(inf))
    bst.n = len(prefix_lst)
    
    return bst
        
        
        