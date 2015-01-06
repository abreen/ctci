# 4.2: Given a directed graph, design an algorithm to find out whether
# there is a route between two nodes.

# This can be done simply by using breadth-first search starting from
# the source vertex.

from graph import Graph, Digraph, Vertex

v1 = Vertex("A")
v2 = Vertex("B")
v3 = Vertex("C")
g = Digraph([v1, v2, v3])

g.link(v1, v2)
g.link(v2, v3)

def route_exists(start, end):
    queue = [n for n in start.neighbors]
    while len(queue) > 0 and end not in queue:
        n = queue.pop(0)
        queue.extend(n.neighbors)

    return end in queue

print(route_exists(v1, v3))     # should be True
print(route_exists(v3, v1))     # should be False

g = Graph([v1, v2, v3])
g.link(v1, v2)
g.link(v2, v3)

print(route_exists(v3, v1))     # should be True
