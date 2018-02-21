from linkedlist import Node

class BST(object):
    def __init__(self, arr):
        self.root = Node(arr[len(arr)/2])
        self.left = BST(arr[0:len(arr)/2])
        self.right = BST(arr[len(arr)/2:-1])
        return self.root

    def get_node(self, value):
        return True
def main(argv):
    tree = BST([1,2,3,4,5])
    import pdb; pdb.set_trace()
if __name__ == '__main__':
    main(sys.argv[1:])
