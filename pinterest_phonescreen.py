# Write a function that takes in the image and returns the coordinates of the rectangle of 0’s -- either top-left and bottom-right; or top-left, width, and height.

# Sample output:
# x: 3, y: 2, width: 3, height: 2 or
# 3,2 5,3


image = [
  [1, 0, 1, 1, 1, 1, 1],
  [1, 0, 0, 1, 0, 1, 1],
  [1, 1, 1, 0, 0, 0, 1],
  [1, 0, 1, 1, 0, 1, 1],
  [1, 0, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 0, 0, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
]



def find_beginning(image, visited_matrix, start_row, start_column):
    row = 0
    while row < len(image):
        col = 0
        while col < len(image[0]):
            if image[row][col] == 0 and [row,col] not in visited_matrix:
                return row, col
            col += 1
        row += 1
    return row, col

# O(w*l*2)
# O(w*l)
# def find_rectangle(image):
#     visited_matrix = [[]]
#     results = []
#     start_row, start_column = find_beginning(image, visited_matrix, 0, 0)
#     while start_row < len(image) or start_column < len(image[0]):
#         end_row = start_row
#         while end_row < len(image) and image[end_row][start_column] == 0:
#             end_column = start_column
#             while end_column < len(image[0]) and image[start_row][end_column] == 0:
#                 visited_matrix.append([end_row, end_column])
#                 end_column += 1
#             end_row += 1
#         results.append([start_row, start_column, end_row-1, end_column-1])
#         start_row, start_column = find_beginning(image, visited_matrix, start_row, start_column)
#     return results
    # return start_column, start_row, end_column-1, end_row-1

# for res in find_rectangle(image):
#     print res

def find_adjacent_points(row, column, matrix):
    points = []
    if 0 <= row + 1< len(matrix) and matrix[row][column] == 0:
        points.append([row + 1, column])

    if 0 <= row - 1< len(matrix) and matrix[row][column] == 0:
        points.append([row -1, column])
    if 0 <= column - 1< len(matrix[0]) and matrix[row][column] == 0:
        points.append([row , column-1])
    if 0 <= column + 1< len(matrix[0]) and matrix[row][column] == 0:
        points.append([row , column+1])
    return points


def find_shape(image):
    visited_matrix = [[]]
    results = []
    start_row, start_column = find_beginning(image, visited_matrix, 0, 0)
    while start_row < len(image) or start_column < len(image[0]):
        result = []
        to_visit = [[start_row, start_column]]
        print to_visit
        while len(to_visit) > 0:
            next_row, next_column = to_visit.pop()
            print next_row, next_column
            result.append(next_row, next_column)
            for point in find_adjacent_points:
                to_visit.append(point)



    results.append(result)
    start_row, start_column = find_beginning(image, visited_matrix, start_row, start_column)
    return results

find_shape(image)
