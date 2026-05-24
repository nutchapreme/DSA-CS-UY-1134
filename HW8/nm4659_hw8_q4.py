from BinarySearchTreeMap import BinarySearchTreeMap
def find_min_abs_difference(bst):
    if bst.root is None:
        return None
    store = [node.item.key for node in bst.inorder()]
    
    min_diff = float('inf')
    for i in range(1,len(store)):
        min_diff = min(min_diff, abs(store[i]-store[i-1]))
        
    return min_diff