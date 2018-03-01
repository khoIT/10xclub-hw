def matrix_region_sum(matrix, topleft, bottomright):
    sum = 0
    row_idx = topleft[1]
    while row_idx <= bottomright[1]:
        col_idx = topleft[0]
        while col_idx <= bottomright[0]:
            sum += matrix[row_idx][col_idx]
            col_idx += 1
        row_idx += 1
    return sum
