from listnode import ListNode

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
        new_node = ListNode(data)

        if self.head:
            trav = self.head
            while trav.next:
                trav = trav.next

            trav.next = new_node
        else:
            self.head = new_node

    def get(self, index):
        """Given a zero-based index, return the data at that position."""
        i = 0
        trav = self.head
        while trav:
            if i == index:
                return trav.data
            i += 1
            trav = trav.next

        return None

    def __len__(self):
        i = 0
        trav = self.head
        while trav:
            i += 1
            trav = trav.next
        return i
