def is_zero_matrix(matrix):
    for row in matrix:
        for element in row:
            if element != 0:
                return False
    return True
