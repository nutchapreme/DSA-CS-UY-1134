from LinkedBinaryTree import LinkedBinaryTree

def min_and_max(bin_tree):
    def subtree_min_and_max(root):
        if root.left is None and root.right is None:
            return root.data, root.data
        elif root.left is not None and root.right is None:
            left = subtree_min_and_max(root.left)
            return min(left[0],root.data), max(left[1],root.data)
        elif root.left is None and root.right is not None:
            right = subtree_min_and_max(root.right)
            return min(right[0],root.data), max(right[1],root.data)
        else:
            left = subtree_min_and_max(root.left)
            right = subtree_min_and_max(root.right)
            return min(left[0], right[0],root.data), max(left[1], right[1],root.data)
    if bin_tree.root is None:
        raise Exception("The tree is empty.")
    return subtree_min_and_max(bin_tree.root)      

        
        
        