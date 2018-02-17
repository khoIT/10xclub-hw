'''Stock Buy Sell to Maximize Profit. Difficulty: 3.1
The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling in those days.
For example, if the given array is
[100, 180, 260, 310, 40, 535, 695],
the maximum profit can earned by buying on day 0, selling on day 3.
Again buy on day 4 and sell on day 6.

If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.
'''
def max_stock_price(arr):
    high = arr[0]
    low = arr[0]
    max_distance = high - low
    small_index = large_index = 0
    low_index = high_index = 0
    for idx, price in enumerate(arr):
        if price < low:
            low = high = price
            low_index = high_index = idx
        if price > high:
            high = price
            high_index = idx
            if high - low > max_distance:
                max_distance = high-low
                small_index = low_index
                large_index = high_index
    return small_index, large_index, max_distance
