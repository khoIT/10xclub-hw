# return the median of the stream as more num being added
# if total number of stream is odd => return the middle number
# if total number of stream is even => return avg of the two middle numbers
import copy

class Heap(object):
    def __init__(self, arr, heap_kind):
        self.arr = copy.copy(arr)
        self.heap_kind = heap_kind
        self.heapify()

    def siftDown(self, idx):
        lc_idx = idx*2 + 1
        rc_idx = idx*2 + 2
        priority_idx = idx

        if self.heap_kind == 'max_heap':
            if lc_idx < len(self.arr) and self.arr[lc_idx] > self.arr[priority_idx]:
                priority_idx = lc_idx
            if rc_idx < len(self.arr) and self.arr[rc_idx] > self.arr[priority_idx]:
                priority_idx = rc_idx
        else:
            if lc_idx < len(self.arr) and self.arr[lc_idx] < self.arr[priority_idx]:
                priority_idx = lc_idx
            if rc_idx < len(self.arr) and self.arr[rc_idx] < self.arr[priority_idx]:
                priority_idx = rc_idx
        if priority_idx != idx:
            self.arr[idx], self.arr[priority_idx] = self.arr[priority_idx], self.arr[idx]
            self.siftDown(priority_idx)

    def heapify(self):
        idx = len(self.arr) / 2
        while idx >= 0:
            self.siftDown(idx)
            idx -= 1
    def parent_idx(self, idx):
        if idx % 2 == 0:
            return (idx - 2) /2
        return idx / 2

    def add(self, num):
        self.arr.append(num)
        num_idx = len(self.arr) - 1
        parent_idx = self.parent_idx(num_idx)
        while parent_idx >=0 and self.arr[parent_idx] < self.arr[num_idx]:
            self.arr[parent_idx], self.arr[num_idx] = self.arr[num_idx], self.arr[parent_idx]
            num_idx = parent_idx
            parent_idx = self.parent_idx(num_idx)

    def peek(self):
        self.arr[0]

median_arr = []
min_heap = Heap([], 'min_heap') # of bigger nums
max_heap = Heap([], 'max_heap') # of smaller nums
num_elements = 0
def median_in_a_stream(num):
    if num_elements == 0:
        max_heap.add(num)
        num_elements += 1
        return num
    if num_elements % 2 == 0:
        if num < max_heap.peek()
        return max_heap.peek()
    print median_arr

if __name__ == '__main__':
    # test heap works
    arr = [2,5,4,10,7,3,8]
    max_heap = Heap(arr, 'max_heap')
    min_heap = Heap(arr, 'min_heap')
    print max_heap.arr
    max_heap.add(9)
    print max_heap.arr
    print min_heap.arr

    # test median_in_a_stream
    # while True:
    #     num = int(raw_input('Next int into stream'))
    #     print("Median of stream after insert {} should be: {}".format(num, median_in_a_stream(num)))
