def binary_search(arr, target):
    position_buffer = 0
    while len(arr) > 0:
        mid = len(arr)/2
        if target > arr[mid]:
            position_buffer += len(arr[:mid]) + 1
            arr = arr[mid+1:]
        elif target < arr[mid]:
            arr = arr[:mid]
        else:
            return mid + position_buffer
    return None
