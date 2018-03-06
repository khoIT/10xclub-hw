from collections import deque

class Vertex(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col

class Graph(object):
    def __init__(self):
        self.V = [] # list of vertex
        self.adjacent = {}

    def adjacent_vertices(self, vertex):
        v1 = Vertex(vertex.row, vertex.col-1)
        v2 = Vertex(vertex.row-1, vertex.col)
        v3 = Vertex(vertex.row, vertex.col+1)
        v4 = Vertex(vertex.row+1, vertext.col)
        return [v1, v2, v3, v4]

    def build_graph(self, arr):
    '''Given an 2d array of true and false. Build the graph, each ele in array is a vertice
    '''
        for row_idx in xrange(0, len(arr)):
            for col_idx in xrange(0, len(arr[0])):
                if arr[row_idx][col_idx] == 1:
                    vertex = Vertex(row_idx, col_idx)
                    self.V.append(vertex)
                    for adj in self.adjacent_vertices(vertex):
                        if adj.row < len(arr) and adj.col < len(arr[0]) and arr[adj.row][adj.col] == 1:
                            self.adjacent[vertex].append(adj)

    def build_shortest_path(self, arr, source):
        return True

    def printGraph(self):
        for v in self.V:
            print("Node {},{} has adjacents: {}".format(v.row, v.col, self.adjacent[v]))

if __name__ == "__main__":
    g = Graph()
    array_input = [[0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
                   [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                   [0, 1, 0, 1, 1, 0, 0, 1, 0, 0],
                   [1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
                   [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                   [1, 0, 0, 1, 1, 0, 1, 0, 0, 1,],
                   [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                   [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
                   [0, 1, 0, 0, 1, 1, 1, 0, 0, 0],
                   [1, 1, 1, 1, 1, 1, 1, 0, 0, 1]
    ]
    g.build_graph(array_input)
    g.printGraph()
