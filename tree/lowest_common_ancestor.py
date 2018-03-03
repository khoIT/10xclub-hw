import sys

from binary_search_tree import BST

def lowest_common_ancestor(nodea, nodeb):
    patha = graph_to_root(nodea)
    pathb = graph_to_root(nodeb)
    idx = 0
    print("Path A: {}".format(patha))
    print("Path B: {}".format(pathb))
    while patha[idx] == pathb[idx]:
        if idx == len(patha) - 1 or idx == len(pathb) - 1:
            idx += 1
            break
        idx += 1
    return patha[idx-1]

def graph_to_root(node):
    path = []
    while node is not None:
        path.insert(0, node.value)
        node = node.parent
    return path

def find_root(node):
    while node.parent is not None:
        node = node.parent
    return node

def lowest_common_ancestor_recursive(nodea, nodeb):
    root = find_root(nodea)
    if root.value < nodea.value and root.value < nodeb.value:
        while root.value < nodea.value and root.value < nodeb.value:
            root = root.right
        return root.value
    elif root.value > nodea.value and root.value > nodeb.value:
        while root.value > nodea.value and root.value > nodeb.value:
            root = root.left
        return root.value
    else:
        return root.value

def main(argv):
    tree = BST([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    tree.preorder_traversal(tree.root)
    nodea = tree.root.left.left
    nodeb = tree.root.right.left.left
    print("Lowest common ancestor of {} and {} is: {}".format(nodea.value, nodeb.value, lowest_common_ancestor(nodea, nodeb)))
    print("Lowest common ancestor of {} and {} is: {}".format(nodea.value, nodeb.value, lowest_common_ancestor_recursive(nodea, nodeb)))
    nodea = tree.root.left.left
    nodeb = tree.root.left.right.left
    print("Lowest common ancestor of {} and {} is: {}".format(nodea.value, nodeb.value, lowest_common_ancestor(nodea, nodeb)))
    print("Lowest common ancestor of {} and {} is: {}".format(nodea.value, nodeb.value, lowest_common_ancestor_recursive(nodea, nodeb)))
    nodea = tree.root.left.left
    nodeb = tree.root.left.left.right
    print("Lowest common ancestor of {} and {} is: {}".format(nodea.value, nodeb.value, lowest_common_ancestor(nodea, nodeb)))
    print("Lowest common ancestor of {} and {} is: {}".format(nodea.value, nodeb.value, lowest_common_ancestor_recursive(nodea, nodeb)))
if __name__ == "__main__":
    main(sys.argv[1:])
