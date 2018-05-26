#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def kthSmallestInBST(t, k):
    k, value = kthSmallestInBSTrecur(t, k, None)
    return value

def kthSmallestInBSTrecur(t, k, val):
    if t.left is None and t.right is None:
        if k > 1:
            return k-1, None
        else:
            return k-1, t.value

    if t.left is not None:
        k, val = kthSmallestInBSTrecur(t.left, k, val)
    if k == 0:
        return k, val
    elif k == 1:
        return k-1, t.value
    else:
        k -= 1
    if t.right is not None:
        k, val = kthSmallestInBSTrecur(t.right, k, val)

    return k, val
