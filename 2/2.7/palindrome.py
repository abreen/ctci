# 2.7: Implement a function to check if a linked list is a palindrome.

# A palindrome is a sequence that reads the same way forwards as it
# does backwards. In other words, for a sequence S, S == reverse(S).

# I'll consider the acyclic linked list case. For doubly linked lists,
# this is simple. Find the end of the linked list and then send two
# pointers towards each other, from the front and rear, comparing the
# node's data to each other. If they always match, return true.

# For singly linked lists, another simple solution can be to use a
# stack. Make one pass to push the data of each node onto a stack,
# and then use a second pass from the front of the list, and repeatedly
# pop the data off the stack to see if they match. If the stack ends
# up empty without any mismatches, the list is a palindrome.

from linkedlist import LinkedList

def is_palindrome(list_):
    stack = []
    n = list_.head
    while n is not None:
        stack.append(n)
        n = n.next

    n = list_.head
    while len(stack) > 0:
        m = stack.pop()
        if n.data != m.data:
            return False
        else:
            n = n.next

    return True

# Note: the book's solution uses the turtle/hare approach to determine
# the halfway point of the list, only pushing nodes from the turtle pointer
# to the stack. This way, every node will be considered only once.
