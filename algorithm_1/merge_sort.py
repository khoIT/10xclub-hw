def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)/2
    sorted_left = merge_sort(arr[:mid])
    sorted_right = merge_sort(arr[mid:])
    return merge(sorted_left, sorted_right)

def merge(left, right):
    idx_left = 0
    idx_right = 0
    return_arr = []
    while idx_left < len(left) and idx_right < len(right):
        if left[idx_left] > right[idx_right]:
            return_arr.append(right[idx_right])
            idx_right += 1
        else:
            return_arr.append(left[idx_left])
            idx_left += 1
    while idx_left < len(left):
        return_arr.append(left[idx_left])
        idx_left += 1
    while idx_right < len(right):
        return_arr.append(right[idx_right])
        idx_right += 1
    return return_arr
