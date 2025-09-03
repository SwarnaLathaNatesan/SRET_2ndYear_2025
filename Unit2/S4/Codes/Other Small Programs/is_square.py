def is_square(matrix):
    for row in matrix:
        if len(row) != len(matrix):
            return False
    return True
