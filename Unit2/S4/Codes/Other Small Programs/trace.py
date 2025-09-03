def trace(matrix):
    total = 0
    for i in range(min(len(matrix), len(matrix[0]))):
        total += matrix[i][i]
    return total
