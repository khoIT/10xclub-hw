import sys

from binary_search_tree import BST

'''Given a random node in a tree.
Return it's next laregest node.
Each node has access to its parent
'''
def smallest_in_right_subtree(node):
    if node.left:
        return smallest_in_right_subtree(node.left)
    else:
        return node

def next_largest(node):
    if node.right:
        return smallest_in_right_subtree(node.right)
    while True:
        parent = node.parent
        if parent is None:
            return node
        if parent.left == node:
            return parent
        else:
            node = node.parent

def main(argv):
    tree = BST([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    tree.preorder_traversal(tree.root)
    print("Next largest value of node {} is: {}".format(tree.root.left.left.value, next_largest(tree.root.left.left).value))
    print("Next largest value of node {} is: {}".format(tree.root.left.right.value, next_largest(tree.root.left.right).value))
    print("Next largest value of node {} is: {}".format(tree.root.left.left.right.value, next_largest(tree.root.left.left.right).value))
if __name__ == "__main__":
    main(sys.argv[1:])
