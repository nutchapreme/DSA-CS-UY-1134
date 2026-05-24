# Author: Dorien Zhang
# Recitation 04/24/25 Code for testing

#--------------------------- Making trees and stuff ---------------------------#

def why_do_you_make_me_do_this(root):
    ret_val = LinkedBinaryTree(root)

    # left subtree
    node2 = LinkedBinaryTree.Node(2)
    root.left = node2
    node2.parent = root
    node3 = LinkedBinaryTree.Node(3)
    node2.left = node3
    node3.parent = node2
    node9 = LinkedBinaryTree.Node(9)
    node3.right = node9
    node9.parent = node3
    node1 = LinkedBinaryTree.Node(1)
    node9.left = node1
    node1.parent = node9

    # Build right subtree
    node5 = LinkedBinaryTree.Node(5)
    root.right = node5
    node5.parent = root
    node7 = LinkedBinaryTree.Node(7)
    node5.left = node7
    node7.parent = node5
    node6 = LinkedBinaryTree.Node(6)
    node5.right = node6
    node6.parent = node5
    node8 = LinkedBinaryTree.Node(8)
    node6.left = node8
    node8.parent = node6

    return ret_val

def why_do_you_make_me_bst():
    ret_val = BinarySearchTreeMap()
    ret_val.insert(6, None)
    ret_val.insert(3, None)
    ret_val.insert(9, None)
    ret_val.insert(2, None)
    ret_val.insert(1, None)
    ret_val.insert(4, None)
    ret_val.insert(5, None)
    ret_val.insert(7, None)
    ret_val.insert(8, None)
    ret_val.insert(11, None)
    ret_val.insert(10, None)
    ret_val.insert(12, None)

    return ret_val

def i_hate_everything(root): # returns example from monodata subtrees
    ret_val = LinkedBinaryTree(root)

    # left subtree
    node1 = LinkedBinaryTree.Node(1)
    root.left = node1
    node1.parent = root
    node5a = LinkedBinaryTree.Node(5)
    node1.left = node5a
    node5a.parent = node1
    node5b = LinkedBinaryTree.Node(5)
    node1.right = node5b
    node5b.parent = node1

    # right subtree
    node5c = LinkedBinaryTree.Node(5)
    root.right = node5c
    node5c.parent = root
    node5d = LinkedBinaryTree.Node(5)
    node5c.right = node5d
    node5d.parent = node5c

    return ret_val