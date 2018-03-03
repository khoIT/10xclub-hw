def heapsort(arr):
    heap = heapify(arr)
    idx = len(heap) - 1
    new_arr = []
    while idx >= 0:
        heap[0], heap[idx] = heap[idx], heap[0]
        siftDown(0, heap, idx)
        idx -= 1

    return heap

def siftDown(i, arr, end):
    left_idx = i*2 + 1
    right_idx = i*2 + 2
    largest_idx = i
    if left_idx < end and arr[left_idx] > arr[largest_idx]:
        largest_idx = left_idx
    if right_idx < end and arr[right_idx] > arr[largest_idx]:
        largest_idx = right_idx
    if largest_idx != i:
        arr[i], arr[largest_idx] = arr[largest_idx], arr[i]
        i = largest_idx
        siftDown(i, arr, end)

def heapify(arr):
    idx = len(arr)/2 - 1
    while idx >= 0:
        siftDown(idx, arr, len(arr))
        # print arr, idx
        idx -= 1
    return arr
