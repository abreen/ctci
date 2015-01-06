# 4.3: Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height.

# To realize this, we will note that, for any sequence of sorted, ascending
# unique integers, there is at least one binary search tree with minimal
# height containing those integers. The sequence of integers is created
# by an in-order traversal of that tree. Therefore, our algorithm will
# be working backwards (in a sense) to create the tree.

from bst import BinarySearchTree
from treenode import TreeNode

asc_odd = [2, 3, 6, 8, 9, 14, 16]

# For this list above, the root should be the middle element, 8. Then
# we can take the middle element of the right part (the slice of
# the list starting after 8 and continuing to the end) as the right
# subtree's root. This continues recursively.

# We can write a recursive algorithm that takes the list as a
# parameter and returns the root of the new tree.

def middle(list_):
    return list_[len(list_) // 2]

def left(list_):
    return list_[:len(list_) // 2]

def right(list_):
    return list_[(len(list_) // 2) + 1:]

def from_sorted(list_):
    bst = BinarySearchTree()
    bst.root = _make_tree(list_)
    return bst

def _make_tree(list_):
    if len(list_) == 0:
        return None

    root = TreeNode(middle(list_))
    root.right = _make_tree(right(list_))
    root.left = _make_tree(left(list_))

    return root


tree = from_sorted(asc_odd)
print(tree)                         # should show the whole list
print(tree.root)                    # should be 8
print(tree.root.left)               # should be 3
print(tree.root.right)              # should be 14

asc_even = [2, 4, 5, 7]
tree = from_sorted(asc_even)
print(tree)
print(tree.root)                    # should be 5
print(tree.root.left)               # should be 4
print(tree.root.right)              # should be 7

# I mentioned before that, for each ascending sequence of integers there is
# "at least" one minimally sized tree that can be formed from the sequence.
# Note that, for a source list of even length, more than one valid tree
# can be created. The tree above has a height of 2 --- minimal for this number
# of nodes --- and its root is 5. Another valid tree is the tree whose root
# is actually 4, and its right subtree is rooted at 5.

# This algorithm runs in O(n) time, very simply. No other space than the
# tree nodes is needed.
