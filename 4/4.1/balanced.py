# 4.1: Implement a function to check if a binary tree is balanced. For the
# purposes of this question, a balanced tree is defined to be a tree such
# that the heights of the two subtrees of any node never differ by more
# than one.

from binarytree import BinaryTree

def is_balanced(tree):
    return _is_balanced(tree.root)

def _is_balanced(node):
    height_left = node.left.height() if node.left else 0
    height_right = node.right.height() if node.right else 0

    if abs(height_left - height_right) > 1:
        return False
    else:
        return _is_balanced(node.left) and _is_balanced(node.right)

# A more efficient solution suggested by the book involves a function
# that does both height and balance checking. This is because the
# function above makes many calls to each node's height method. In
# the worst case, a node's height method will be called O(n) times,
# where n is the number of nodes.

def is_balanced(tree):
    return _check_balanced(tree.root)

def _check_balanced(node):
    if node.left is None and node.right is None:
        return 0

    left = _check_balanced(node.left)
    right = _check_balanced(node.right)

    if left == -1 or right == -1:
        return -1

    if abs(left - right) > 1:
        return -1

    return max(left, right) + 1

# This version runs in O(n) time.
