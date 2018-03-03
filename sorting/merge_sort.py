# recursive
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)/2
    sorted_left = merge_sort(arr[:mid])
    sorted_right = merge_sort(arr[mid:])
    return merge(sorted_left, sorted_right)

def merge(arr1, arr2):
    i1 = 0
    i2 = 0
    return_arr = []
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] > arr2[i2]:
            return_arr.append(arr2[i2])
            i2 += 1
        else:
            return_arr.append(arr1[i1])
            i1 += 1
    while i1 < len(arr1):
        return_arr.append(arr1[i1])
        i1 += 1
    while i2 < len(arr2):
        return_arr.append(arr2[i2])
        i2 += 1
    return return_arr


# iterative
def merge_sort_iterative(arr):
    work_queue = []
    for ele in arr:
        work_queue.append([ele])
    while len(work_queue) > 1:
        arr1 = work_queue.pop(0)
        arr2 = work_queue.pop(0)
        merged = merge(arr1, arr2)
        work_queue.append(merged)
    return work_queue.pop()
