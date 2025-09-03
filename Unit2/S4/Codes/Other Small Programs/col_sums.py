def col_sums(matrix):
    sums = []
    for j in range(len(matrix[0])):
        sums.append(sum(matrix[i][j] for i in range(len(matrix))))
    return sums
