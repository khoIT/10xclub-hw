# Triangle Data Structure (not a binary tree)
#       4
#      / \
#     2   3
#    / \ / \
#   3   4   5
#  / \ / \ / \
# 2   5   4   9

# array representation of triangle
T = [
  [4],     #    [21]
  [2,3],   #    [11,17]
  [3,4,5], # => [8,9,14]
  [2,5,4,9]
]

# Each node has 2 children, and can have one or two parents
# One possible path P_example = 4 -> 3 -> 5 -> 4
# For each path P we can compute a Sum(P)
# Sum(P) is defined as the sum of all the values in the nodes of P

# Sum(P_example) = 4 + 3 + 5 + 4
#                = 16

# Exercise:
# Write a function that returns the maximum possible value of Sum(P) for the triangle above
# The answer should be 21, but your function should work for any triangle supplied.

def maximum_value(arr):
    import copy
    max_arr = copy.deepcopy(arr)
    index = len(arr)-2 # 2

    while index >=0:
        j = 0
        below_arr = max_arr[index+1]
        # print below_arr
        # print arr[index]
        new_arr = []
        while j<len(arr[index]):
            # print "running j {}".format(j)
            to_add = max(below_arr[j], below_arr[j+1])
            new_arr.append(arr[index][j] + to_add)
            j += 1
        # print "done with row {}".format(index)
        max_arr[index] = new_arr
        index -= 1
    return max_arr


print(maximum_value(T))


reduce(reduce_rows,T)
