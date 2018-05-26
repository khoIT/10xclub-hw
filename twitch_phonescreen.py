"""
Write a function that takes two strings as input
and returns the index of the first occurence
of the first string in the second
"""
"""
first_occurence("a","abc") => 0
first_occurence("b","abc") => 1
first_occurence("","abc")  => 0
first_occurence("abc","a") => None
"""

def first_occurence(str_1, str_2):
    idx = 0
    if len(str_1) ==0:
        return 0
    if len(str_1) > len(str_2):
        return None

    while idx < len(str_2):
        inner_idx = 0
        while inner_idx < len(str_1) and idx + inner_idx < len(str_2) and str_2[idx+inner_idx] == str_1[inner_idx]:
            inner_idx += 1
        if inner_idx == len(str_1):
            return idx
        idx += 1
    return None


# print (first_occurence("a","abc") == 0)
# print (first_occurence("b","abc") == 1)
# print (first_occurence("c","abc") == 2)
# print (first_occurence("","abc")  == 0)
# print (first_occurence("abc","a") == None)
# print (first_occurence("cd","abc") == None)
# print (first_occurence("acde","abc") == None)
# print (first_occurence("e","abc") == None)
# print (first_occurence("abc","abc") == 0)
# print (first_occurence("bc","abcd") == 1)
# print (first_occurence("bcd","abcd") == 1)

from collections import namedtuple

"""
   4
  / \
 3   5
    / \
   7   1



lca(r, 7, 1) -> 5
lca(r, 7, 3) -> 4
lca(r, 7, 5) -> 5
lca(r, 7, 7) -> 7

"""

Node = namedtuple('Node', ['value', 'left', 'right'])
def findPath(root, node, path):
    if root is None:
        return False
    path.append(root)
    if root.value == node:
        return True

    if (root.left != None and findPath(root.left, node, path)) or (root.right != None and findPath(root.right, node, path)):
        return True
    path.pop()
    return False


def lca(root, left, right):
    left_path = []
    right_path = []
    if (not findPath(root, left, left_path)) or not (findPath(root, right, right_path)):
        return -1
    i = 0
    while i < len(left_path)  and i < len(right_path):
        if left_path[i].value != right_path[i].value:
            break
        i += 1

    return left_path[i-1].value

def mktree():
    seven = Node(7, None, None)
    one   = Node(1, None, None)
    three = Node(3, None, None)
    five  = Node(5, seven, one)
    return Node(4, three, five)

# tests here
if __name__ == "__main__":
    root = mktree()
    print "haha", lca(root, 7, 1)
