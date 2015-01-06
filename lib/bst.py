from treenode import TreeNode
from binarytree import BinaryTree

class BinarySearchTree(BinaryTree):
    def add(self, data):
        new_node = TreeNode(data)

        if not self.root:
            self.root = new_node
            return

        trav = self.root
        while True:
            if data < trav.data:
                if not trav.left:
                    trav.left = new_node
                    return

                trav = trav.left

            elif data > trav.data:

                if not trav.right:
                    trav.right = new_node
                    return

                trav = trav.right

            else: # duplicate
                return


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.add(2)
    tree.add(3)
    tree.add(8)
    print(tree)
