
'''  SET A
1. Unique items
 Write a function that takes in an array. It should return a new array
 containing only the elements that were unique in the original array.
 For example:
 ary = [1, 5, 5, 7, 16, 8, 1, 8]
 unique = unique_items(ary)
 unique # => [7, 16]
'''
from sets import Set

def unique_items(arr):
    count = {}
    output = []
    for item in arr:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    for k,v in count.iteritems():
        if v == 1:
            output.append(k)
    return output

'''3. Ping Pong Filter
 Imagine that we have a filter that goes through an array and removes every other
 element. When it reaches the final element it turns around and does the whole
 process again, this time going from the end to the start. It repeats this
 behavior until there is only one element left.
'''
def ping_pong_filter(arr):
    left = True
    while len(arr) > 1:
        if left:
            del arr[::2]
            left = False
        else:
            del arr[1::2]
            left = True
    return arr

''' SET B
2. Five Sort (hard)
 Write a function that receives an array of numbers as an argument.
 It should return the same array with the fives moved to the end.
 The ordering of the other elements should remain unchanged.
 For example:
 nums = [1, 5, 3, 5, 5, 2, 3]
 sorted = five_sort(nums)
 sorted # => [1, 3, 2, 3, 5, 5, 5]
 Rules
 * You may not, at any time, create a new array.
 * You are only permitted to use a 'while' loop
 * You are not permitted to call any methods on the array. Only the
    use of [], []=, and length are permitted.
'''
def five_sort(arr):
    index = 0
    count_non_5 = 0
    while index < len(arr):
        if arr[index] != 5:
            arr[count_non_5] = arr[index]
            count_non_5 += 1
        index += 1
    while count_non_5 < len(arr):
        arr[count_non_5] = 5
        count_non_5 += 1
    return arr
