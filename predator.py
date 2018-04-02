"""
Predator
- each species has maximum of 1 direct predator
- predator can be inherited
- predator is one way relationship (no mutual predator each other)
- return minimum # of groups such that no species is grouped with its predator (direct or indirect)
"""
# minimum_groups([2, -1, 3, 2]) => 2 ([0,3] and [2] since species index 1 can go with either group)
        # index   0,  1, 2, 3
# minimum_groups([2, -1, 1, 2]) => 3 [0,3] [2] [1] since 1 is a predator of 2 and thus a predator of 0,3, needs to become 3
class Node(object):
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []
    # assume node is root
    def tree_height(self):
        if len(self.children) == 0:
            return 1
        max_height = 0
        for child in self.children:
            if child.tree_height() > max_height:
                max_height = child.tree_height()
        return 1 + max_height

def minimum_groups(arr):
    nodes_map = {}
    for idx, ele in enumerate(arr):
        if idx not in nodes_map:
            node = Node(idx)
            nodes_map[idx] = node
        else:
            node = nodes_map.get(idx)
        if ele == -1:
            continue
        if ele not in nodes_map:
            parent_node =  Node(ele)
            nodes_map[ele] = parent_node
        else:
            parent_node = nodes_map.get(ele)
        node.parent = parent_node
        parent_node.children.append(node)

    root_list = []
    for ele, node, in nodes_map.iteritems():
        if node.parent is None:
            root_list.append(node)

    max_height = 0
    for root in root_list:
        if root.tree_height() > max_height:
            max_height = root.tree_height()
    return max_height

if __name__ == "__main__":
    print minimum_groups([2,8,1,2,2,7,7,9,-1,8,8])
    print minimum_groups([3,-1,0,1])
    print minimum_groups([-1,0,1])
    print minimum_groups([1,-1,3,-1])
