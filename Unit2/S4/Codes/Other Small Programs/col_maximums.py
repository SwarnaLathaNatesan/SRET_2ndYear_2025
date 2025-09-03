def col_maximums(matrix):
    maximums = []
    for j in range(len(matrix[0])):
        maximums.append(max(matrix[i][j] for i in range(len(matrix))))
    return maximums
