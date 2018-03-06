from __future__ import print_function
from collections import deque

class Vertex(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.dist = 0
        self.path_so_far = []

class Graph(object):
    def __init__(self):
        self.V = [] # list of vertex
        self.adjacent = {}

    def adjacent_vertices(self, vertex):
        v1 = Vertex(vertex.row, vertex.col-1)
        v2 = Vertex(vertex.row-1, vertex.col)
        v3 = Vertex(vertex.row, vertex.col+1)
        v4 = Vertex(vertex.row+1, vertex.col)
        return [v1, v2, v3, v4]

    def build_graph(self, arr):
        '''Given an 2d array of true and false. Build the graph, each ele in array is a vertice'''
        for row_idx in xrange(0, len(arr)):
            for col_idx in xrange(0, len(arr[0])):
                if arr[row_idx][col_idx] == 1:
                    vertex = Vertex(row_idx, col_idx)
                    self.V.append(vertex)
                    adj_list = self.adjacent.setdefault(vertex, [])
                    for adj in self.adjacent_vertices(vertex):
                        if 0 <= adj.row < len(arr) and 0 <= adj.col < len(arr[0]) and arr[adj.row][adj.col] == 1:
                            adj_list.append(adj)

    def printGraph(self):
        for v in self.V:
            print("Node {},{} has adjacents:".format(v.row, v.col), end='')
            for adj in self.adjacent[v]:
                print("{},{}; ".format(adj.row, adj.col), end='')
            print('')


    def build_shortest_path_from_source(self, arr, source, end):
        ''' using bfs to find the shortest path '''
        qu = deque()
        qu.append(source)
        visited = set()
        while len(qu) > 0:
            v = qu.popleft()
            print("{}, {}".format(v.row, v.col))
            visited.add((v.row, v.col))
            if v.row == end.row and v.col == end.col:
                return v
            for adj in self.adjacent_vertices(v):
                if (adj.row, adj.col) in visited:
                    continue
                if 0 <= adj.row < len(arr) and 0 <= adj.col < len(arr[0]) and arr[adj.row][adj.col] == 1:
                    adj.path_so_far = v.path_so_far + [(v.row, v.col)]
                    adj.dist = v.dist + 1
                    qu.append(adj)
        return None
if __name__ == "__main__":
    g = Graph()
    array_input = [[0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
                   [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                   [0, 1, 0, 1, 1, 0, 0, 1, 0, 0],
                   [1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
                   [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                   [1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
                   [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                   [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
                   [0, 1, 0, 0, 1, 1, 1, 0, 0, 0],
                   [1, 1, 1, 1, 1, 1, 1, 0, 0, 1]
    ]
    g.build_graph(array_input)

    v = g.build_shortest_path_from_source(array_input, Vertex(9,0), Vertex(0,9))
    if v:
        print(v.path_so_far)
        print(v.dist)
