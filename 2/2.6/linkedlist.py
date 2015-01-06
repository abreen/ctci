class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        s = "["

        trav = self.head
        while trav:
            s += str(trav)
            trav = trav.next

        s += "]"

        return s

    def add(self, data):
        new_node = LinkedList.Node(data)

        if self.head:
            trav = self.head
            while trav.next:
                trav = trav.next

            trav.next = new_node
        else:
            self.head = new_node

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

        def __str__(self):
            return str(self.data)
