""" Find the shortest distance between 3 chars
    aabcdaetac
    0123456789
"""
import argparse
import sys
from sets import Set

class Node(object):
    def __init__(self, char, value):
        self.char = char
        self.value = value

class Heap(object):
    def __init__(self):
        self.max_index = 0
        self.arr = []
        self.dist = -1

    ''' should only get back idx within range of self.arr '''
    def parent_node_idx(self, node_idx):
        if node_idx > 1:
            if node_idx % 2 == 0:
                return node_idx / 2 - 1
            else:
                return node_idx / 2
        else:
            return None

    """ should only return idx within range of self.arr """
    def children_idx(self, node_heap_idx):
        c1_idx = node_heap_idx * 2 + 1
        c2_idx = node_heap_idx * 2 + 2
        if c1_idx < len(self.arr):
            if c2_idx < len(self.arr):
                return c1_idx, c2_idx
            else:
                return c1_idx, None
        else:
            return None, None

    """ add in the newest node and remove the node with same char, which also is the min node at the top right now """
    def add(self, node):
        # only consider adding the new node if it can replace the node with smallest idx
        if node.char != self.arr[0].char
            return None

        # keep track of the newest node idx
        self.max_index = node.value

        # start adding into our heap or self.arr
        self.arr.append(node)
        if len(self.arr) == 1:
            return len(self.arr)
        node_heap_idx = len(self.arr) - 1
        parent_node_idx = self.parent_node_idx(node_heap_idx)
        while parent_node_idx and node.value < self.arr[parent_node_idx].value:
            self.arr[node_heap_idx], self.arr[parent_node_idx] = self.arr[parent_node_idx], self.arr[node_heap_idx]
            node_heap_idx = parent_node_idx
            parent_node_idx = self.parent_node_idx(node_heap_idx)
        return node_heap_idx

    def pop(self):
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        popNode = self.arr.pop(-1)
        node_heap_idx = 0
        if self.arr[0].value > self.arr[1].value:
            self.arr[0], self.arr[1] = self.arr[1], self.arr[0]
        return popNode

    def peek(self):
        return self.arr[0]

def shortest_list(arr, string):
    heap = Heap()
    idx = 0
    while idx < len(string):
        char = string[idx]
        if char in arr:
            heap.add(Node(char, idx))
        idx += 1
    print heap.distance()
def main(argv):

    heap = Heap()
    heap.add(Node('a', 0))
    heap.add(Node('b', 1))
    heap.add(Node('c', 2))
    heap.add(Node('f', 3))
    heap.add(Node('f', 4))
    heap.add(Node('d', 5))
    heap.add(Node('e', 6))
    heap.add(Node('a', 7))
    heap.add(Node('a', 8))
    heap.add(Node('d', 9))
    heap.add(Node('c', 10))

    print heap.distance()


    parser = argparse.ArgumentParser()
    parser.add_argument("--array", "-a", help="list of strings to be included", default="['a', 'c', 'd']")
    parser.add_argument("--string", "-s", help="string to be examined", default="abcdaetac")
    args = parser.parse_args()
    array = args.array
    string = args.string
    # shortest_list(array, string)
if __name__ == '__main__':
    main(sys.argv[1:])
