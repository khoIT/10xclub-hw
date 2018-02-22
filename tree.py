import sys

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_node(self, value):
        if value < self.value:
            if self.left:
                self.left.insert_node(value)
            else:
                self.left = Node(value)
        else:
            if self.right:
                self.right.insert_node(value)
            else:
                self.right = Node(value)
    def lookup(self, value):
        if value == self.value:
            return self
        elif value < self.value:
            self.left.lookup(value)
        elif value > self.value:
            self.right.lookup(value)
        else:
            return False
        
class BST(object):
    def __init__(self, arr):
        self.root = self.__create_tree(arr)

    def __create_tree(self, arr):
        if len(arr) == 0:
            return None
        elif len(arr) == 1:
            return Node(arr[0])
        else:
            node = Node(arr[len(arr)/2])
            node.left = self.__create_tree(arr[0:len(arr)/2])
            node.right = self.__create_tree(arr[len(arr)/2+1:])
        return node

    def get_node(self, value):
        return True

def main(argv):
    tree = BST([1,2,3,4,5,6,7,8,9])
    import pdb; pdb.set_trace()
if __name__ == '__main__':
    main(sys.argv[1:])
