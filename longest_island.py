'''
Given a sequence of Land and water codes, find the longest island you can build by filling the water in between any two lands.
You can build the longest island by choosing a sequence of water to fill, but any number of slots in that sequence.

Example sequence:
L, W, L, W, W, L, W
The Longest sequence length is 4:
Let's fill water at slot 2 (index 1) so it becomes L,L,L,W,W,L,W. The longest L sequence is length 3
Let's fill the two continuous water slots 4,5 (index 3,4) so it becomes L,W,L,L,L,L,W. The longest L sequence is length 4
Let's fill the last water slot. So it becomes L,W,L,W,W,L,L . The longest L sequence now is 2.

Best answer is O(N).
'''
def longest_island_create(arr):
    # the moment see the first L, start counting all the Ws and all the Ls until see another W
    # record the count of Ws and Ls (consecutively) as total length
    # if that length is bigger than max length then update the max-length
    # because it's the longest island that can be created by converting W to L
    index = 0
    while index < len(arr):
        if arr[index] == 'L'
            length = 0
            index += 1
        while arr[index] != 'W':
            length += 1
            index += 1
        while arr[index] != 'L':
            length += 1
            index += 1
        if length + 1 > max_length:
            max_length = length + 1
    return max_length

if __name__ == "__main__":
    longest_island_create(['L', 'W', 'L', 'W', 'W', 'L', 'W'])
