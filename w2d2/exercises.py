""" Find the shortest distance between 3 chars
    aabcdaetac
    0123456789
"""
import sys
from sets import Set

class Node(object):
    def __init__(self, char, idx):
        self.char = char
        self.idx = idx

class Heap(object):
    def __init__(self):
        self.arr = []
        self.dist = -1

    def distance(self):
        if len(self.arr) == 3:
            self.dist = abs(max(self.arr[1].idx, self.arr[2].idx) - self.arr[0].idx)
        return self.dist

    def parent_node_heap_idx(self, node_idx):
        if node_idx > 1:
            if node_idx % 2 == 0:
                return node_idx / 2 - 1
            else:
                return node_idx / 2
        else:
            return 0

    def smaller_children_idx(self, node_heap_idx):
        c1_idx = node_heap_idx * 2 + 1
        c2_idx = node_heap_idx * 2 + 2
        if c1_idx > len(self.arr) and c2_idx > len(self.arr):
            return node_heap_idx
        if self.arr[c1_idx].idx < self.arr[c2_idx].idx:
            return node_heap_idx * 2 + 1
        else:
            return node_heap_idx * 2 + 2

    def add(self, node):
        self.arr.append(node)
        node_heap_idx = len(self.arr) - 1
        if node_heap_idx > 0:
            parent_node_heap_idx = self.parent_node_heap_idx(node_heap_idx)
            parent_node = self.arr[parent_node_heap_idx]
            while node.idx < parent_node.idx and node_heap_idx > 0:
                self.arr[node_heap_idx], self.arr[parent_node_heap_idx] = self.arr[parent_node_heap_idx], self.arr[node_heap_idx]
                node_heap_idx = parent_node_heap_idx
                parent_node_heap_idx = self.parent_node_heap_idx(node_heap_idx)
                parent_node = self.arr[parent_node_heap_idx]

    def pop(self):
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        popNode = self.arr.pop(-1)
        node_heap_idx = 0
        if self.arr[0].idx > self.arr[1].idx:
            self.arr[0], self.arr[1] = self.arr[1], self.arr[0]
        return popNode

    def peek(self):
        return self.arr[0]

def shortest_list(arr, string):
    heap = Heap()
    idx = 0
    seen = Set()
    while idx < len(string):
        char = string[idx]
        if char in arr and char not in seen:
            if len(heap.arr) < len(arr):
                heap.add(Node(char, idx))
            else:
                import pdb; pdb.set_trace()
                heap_distance = heap.distance()
                temp_node = heap.pop()
                if abs(idx - heap.peek().idx) < heap_distance :
                    heap.add(Node(char, idx))
                else:
                    heap.add(temp_node)
            seen.add(char)
        if len(seen) == len(arr):
            seen.remove(heap.peek().char)
        idx += 1


    print heap.distance()
def main(argv):

    # heap = Heap()
    # heap.add(Node('c', 3))
    # heap.add(Node('d', 4))
    # heap.add(Node('a', 0))
    # print heap.distance()
    # heap.pop()
    # heap.add(Node('a', 0))
    # print heap.distance()
    shortest_list(['a','c','d'], 'abcdaetac')
if __name__ == '__main__':
    main(sys.argv[1:])
