def is_identity(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != (1 if i == j else 0):
                return False
    return True
