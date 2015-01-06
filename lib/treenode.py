class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left, self.right = None, None

    def __str__(self):
        return str(self.data)

    def height(self):
        if self.left is None and self.right is None:
            return 0

        left = self.left.height() if self.left else 0
        right = self.right.height() if self.right else 0

        return max(left, right) + 1
