# 4.5: Implement a function to check if a binary tree is a binary
# search tree.

# Recall the binary search tree property: in a binary search tree,
# for any subtree's root, all keys in its left subtree are less than or
# equal to the root's key, and all keys in the right subtree are greater
# than the root's key.

from binarytree import BinaryTree
from bst import BinarySearchTree
from treenode import TreeNode

# The simple approach I can think of is a recursive algorithm that checks
# the necessary conditions on every node in each subtree, given a particular
# root.

def is_bst(tree):
    return _is_bst(tree.root)

def _is_bst(node):
    if node is None:
        return True

    if lte(node.left, node.data) and gt(node.right, node.data):
        return _is_bst(node.left) and _is_bst(node.right)
    else:
        return False

def lte(node, data):
    if node is None:
        return True

    if node.data > data:
        return False

    return lte(node.left, data) and lte(node.right, data)

def gt(node, data):
    if node is None:
        return True

    if node.data <= data:
        return False

    return gt(node.left, data) and gt(node.right, data)

tree = BinaryTree()
bst_tree = BinarySearchTree()
for n in [2, 6, 3, 8, 2, 9]:
    tree.add(n)
    bst_tree.add(n)

print(is_bst(tree))
print(is_bst(bst_tree))

# This works, but it is very inefficient: leaf nodes will be touched
# O(n) times by the lte() or gt() calls before they are reached by the
# is_bst() function in the worst case, when the tree is actually a BST.

# Another approach might be to try to get this done in one traversal
# by setting upper and lower bounds as the recursive calls go deeper.
# If any node's data is outside these bounds, the function returns false
# immediately.

NEGATIVE_INFINITY, INFINITY = "-inf", "inf"

def is_bst(tree):
    return _is_bst(tree.root, INFINITY, NEGATIVE_INFINITY)

def _is_bst(node, upper, lower):
    """Return False if the binary tree starting at this node contains data
    items greater than the upper bound or lower than or equal to the lower
    bound.
    """
    if node is None:
        return True

    if lower != NEGATIVE_INFINITY and node.data <= lower:
        return False
    if upper != INFINITY and node.data > upper:
        return False

    return _is_bst(node.left, node.data, lower) and \
           _is_bst(node.right, upper, node.data)

print(is_bst(tree))
print(is_bst(bst_tree))

# The book includes a solution like this one. It also initially considers an
# approach where an in-order traversal is done to insert data items into an
# array and check that the array is sorted, but that approach does not
# handle duplicates correctly.
