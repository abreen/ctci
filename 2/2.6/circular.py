# 2.6: Given a circular linked list, implement an algorithm which returns
# the node at the beginning of the loop.

# My first idea was to use a hash table for the data in the nodes, if
# possible. Each time a node is visited, insert the node's data into
# the hash table. Before each node is marked as visited, the hash table
# is considered for a node. If the node's data has already been seen,
# that node is the first node to be visited twice. This will run in
# O(n) time, worst-case, if the loop occurs at the end of the linked list.
# However, collisions in the hash table can make insertion into the table
# (and checking the table) potentially worse than O(1) --- it may be, for
# example, O(n). This solution will also use extra space; it gets complicated
# with hash tables, but resizes can be expensive for some implementations
# as well as memory hogging.

# Therefore this may not be a good solution if the size of the linked list is
# not known (a rare condition, but possible), or the only usable hash function
# for the data is very poor, which can lead to many collisions.

# The second idea (and the simplest) is to alter the linked list's node
# class to contain a "visited" Boolean value. When the node is visited,
# its Boolean value is set to true. As soon as a previously visited
# node is seen, that node must be the first node in the loop.

# This is, of course, assuming we are not given some node *inside* the loop,
# since our algorithm will choose that node as the loop's "beginning".

def beginning_circular(list_):
    current = list_.head
    while current.visited is not True:
        current.visited = True
        current = current.next
    return current

# This approach assumes that we can change the underlying data structure.
# It also assumes that all nodes have a visited value of false to begin with!

# If we don't want to make these assumptions, we must come up with a more
# general solution.

# The solution in the book uses a modified turtle/hare approach.
