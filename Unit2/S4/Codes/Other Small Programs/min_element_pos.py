def min_element_pos(matrix):
    min_val = min(min(row) for row in matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == min_val:
                return (i, j)
