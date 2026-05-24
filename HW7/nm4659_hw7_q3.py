def is_height_balanced(bin_tree):
    def is_subtree_height_balanced(root):
        if root is None:
            return (True,0)
        left = is_subtree_height_balanced(root.left)
        right = is_subtree_height_balanced(root.right)
        height = max(left[1], right[1])+1
        if not (left[0] and right[0]) or abs(left[1] - right[1]) > 1:
            return False, height
        return True, height
    if bin_tree.root is None:
        raise Exception("EmptyTree")
    return is_subtree_height_balanced(bin_tree.root)[0]

                
                