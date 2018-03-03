from datetime import datetime
import random, sys

from merge_sort import merge_sort, merge_sort_iterative
def bubble_sort(arr):
    i = 0
    while i < len(arr):
        j = 0
        while j < len(arr)-1:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
        i += 1
    return arr

def insertion_sort(arr):
    i = 0
    while i < len(arr):
        j = 0
        while arr[j] < arr[i] and j < i:
            j += 1
        temp = arr[i]
        # could save this loop by letting j going backwards
        for idx in range(j, i):
            arr[j+1] = arr[j]
        arr[j] = temp
        i += 1
    return arr

def selection_sort(arr):
    idx = 0
    while idx  < len(arr):
        min_idx = idx
        for j in xrange(idx, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[idx], arr[min_idx] = arr[min_idx], arr[idx]
        idx += 1
    return arr

def constructin_array(size):
    arr = []
    for i in xrange(0, size-1):
        # arr[i] = i
        # arr[i] = size-i
        arr.append(random.randrange(0, size))
    return arr

def time_a_function(func, arg):
    now = datetime.now()
    arg = func(arg)
    print "{} took {}".format(func.__name__, datetime.now() - now)
    return arg

if __name__ == "__main__":
    arr = constructin_array(3000)
    print arr
    time_a_function(bubble_sort, arr)
    time_a_function(insertion_sort, arr)
    time_a_function(selection_sort, arr)
    time_a_function(merge_sort, arr)
    time_a_function(merge_sort_iterative, arr)
    print ("Sorted arr: {}".format(arr))
