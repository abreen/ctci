class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def __str__(self):
        return name


class Graph:
    def __init__(self, vertices = None):
        if vertices:
            self.vertices = vertices
        else:
            self.vertices = []

    def link(self, v1, v2):
        v1.neighbors.append(v2)
        v2.neighbors.append(v1)


class Digraph(Graph):
    def link(self, v1, v2):
        v1.neighbors.append(v2)

