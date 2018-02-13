# Set 1.a
def move_zeros(arr):
    front = 0
    num_zeros = 0
    back = len(arr)-1-num_zeros
    while front != back:
        while arr[front] != 0:
            front += 1
        arr[front], arr[back] = arr[back], arr[front]
        num_zeros += 1
        back = len(arr)-1-num_zeros
    return arr

def random(num):

# Set 1.b
def binary(num):
    if num == 0:
        return '0'
    while num > 0:
        return binary(num/2) + str(num % 2)

def binary_non_recursive(num):
    if num == 0:
        return '0'
    result = ""
    while num > 0:
        result = str(num % 2) + result
        num /= 2
    return result
# what about negative, waht about -0.5

def permutation(arr):
    # [1,2,3] => [[1,2,3], [1,3,2], [2,1,3],[2,3,1], [3,1,2],[3,2,1]]
    # [1,2,3,4] => [[1,2,3,4], [1,2,4,3], [1,3,2,4],[1,3,4,2], [1,4,2,3],[1,4,3,2]]

def permutation_iterator
    value_size = 6
    data = [0,0,0,0] # where length of data is number of elements in permutation
