def knapsack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i][w] == 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K

if __name__ == "__main__":
    W = 6
    n = 3
    val = [60, 200, 30]
    wt = [3,1,2]

    K = knapsack(W, wt, val, 3)
    for row in K:
        print row
