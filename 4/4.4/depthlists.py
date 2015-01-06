# 4.4: Given a binary tree, design an algorithm which creates a linked list
# of all the nodes at each depth (e.g., if you have a tree with depth D,
# you'll have D linked lists).

# My first idea would be to use a stateful recursive function that adds nodes
# to a particular list whenever it reaches a node at that depth. The recursive
# function could do a simply depth-first traversal.

from linkedlist import LinkedList
from listnode import ListNode
from binarytree import BinaryTree

depths = LinkedList()

def make_depth_lists(tree):
    _make_depth_lists(tree.root, 0)

def _make_depth_lists(node, depth):
    if len(depths) == depth:
        # have not yet reached this depth
        # we make a new LinkedList for this depth
        list_ = LinkedList()
        list_.add(node)

        depths.add(list_)

    else:
        list_ = depths.get(depth)
        list_.add(node)

    if node.left:
        _make_depth_lists(node.left, depth + 1)

    if node.right:
        _make_depth_lists(node.right, depth + 1)


tree = BinaryTree()
for n in [2, 6, 3, 8, 2, 9]:
    tree.add(n)

make_depth_lists(tree)
print(depths)


# This algorithm runs in O(n), where n is the number of nodes in the tree.
# It also uses O(n) more space for the nodes in the depth lists.
