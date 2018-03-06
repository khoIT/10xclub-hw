def sort_list_of_tuples(arr):
    # [('a', 3), ('b', 2), ('c',1)] => [('c', 1), ('b', 2), ('a', 3)]
    if len(arr) <= 1:
        return arr
    if len(arr) % 2 != 0:
        mid = len(arr)/2
    else:
        mid = len(arr)/2 -1
    sorted_left = sort_list_of_tuples(arr[:mid+1])
    sorted_right = sort_list_of_tuples(arr[mid+1:])
    return merge(sorted_left, sorted_right)

def merge(half_1, half_2):
    idx_1 = 0
    idx_2 = 0
    arr = []
    while idx_1 < len(half_1) and idx_2 < len(half_2):
        if half_1[idx_1][1] < half_2[idx_2][1]:
            arr.append(half_1[idx_1])
            idx_1 += 1
        else:
            arr.append(half_2[idx_2])
            idx_2 += 1
    while idx_1 < len(half_1):
        arr.append(half_1[idx_1])
        idx_1 += 1
    while idx_2 < len(half_2):
        arr.append(half_2[idx_2])
        idx_2 += 1
    return arr

if __name__ == "__main__":
    arr = sort_list_of_tuples([('a', 5),('b',4),('c', 2),('d',3),('e',1)])
    print arr
