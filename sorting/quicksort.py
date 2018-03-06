def quick_sort(arr):
    print quick_sort_with_index(arr, 0, len(arr)-1)

def quick_sort_with_index(arr, first, last):
    if first < last:
        mid = partition(arr, first, last)
        quick_sort_with_index(arr, first, mid)
        quick_sort_with_index(arr, mid+1, last)
def partition(arr, first, last):

    pivotValue = arr[first]
    left_mark = first+1
    right_mark = last
    done = False
    while done is False:
        while left_mark <= right_mark and arr[left_mark] <= pivotValue:
            left_mark += 1
        while right_mark >= left_mark and arr[right_mark] > pivotValue:
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            arr[left_mark], arr[right_mark] = arr[right_mark], arr[left_mark]
        print arr
    arr[first], arr[right_mark] = arr[right_mark], arr[first]
    return right_mark

if __name__ == "__main__":
    quick_sort([4,3,10,1,5,2,6,9])
