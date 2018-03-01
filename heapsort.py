# [5,4,1,2,6,4]
def heapsort(arr):
    # heapify make sure max element is at left most
    heap = []
    for ele in arr:
        heap.append(ele)
        heap = siftdown(heap, 0)
    return heap

def bigger_child_idx(arr, idx):
    if idx*2+1 >= len(arr):
        return None
    if idx*2+2 >= len(arr):
        return idx*2+1
    if arr[idx*2+1] > arr[idx*2+2]:
        return idx*2+1
    else:
        return idx*2+2

def siftdown(arr, idx):
    import pdb; pdb.set_trace()    
    arr[idx], arr[-1] = arr[-1], arr[idx]
    child_idx = bigger_child_idx(arr, idx)

    while child_idx and arr[child_idx] > arr[idx]:
        arr[idx], arr[child_idx] = arr[child_idx], arr[idx]
        idx = child_idx
        child_idx = bigger_child_idx(arr, idx)

    return arr
