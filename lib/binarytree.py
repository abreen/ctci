from treenode import TreeNode

class BinaryTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def __nodestr__(node):
        if not node:
            return ""

        right = BinaryTree.__nodestr__(node.right)
        left = BinaryTree.__nodestr__(node.left)

        s = ""
        if left:
            s += str(left) + " "
        s += str(node)
        if right:
            s += " " + str(right)

        return s

    def __str__(self):
        return "[" + BinaryTree.__nodestr__(self.root) + "]"

    def add(self, data):
        new_node = TreeNode(data)

        if not self.root:
            self.root = new_node
            return

        trav = self.root
        while trav.left and trav.right:
            if trav.right.height() < trav.left.height():
                trav = trav.right
            else:
                trav = trav.left

        if trav.left is None:
            trav.left = new_node
        else:
            trav.right = new_node


if __name__ == '__main__':
    tree = BinaryTree()
    tree.add(2)
    tree.add(3)
    tree.add(8)
    print(tree)
