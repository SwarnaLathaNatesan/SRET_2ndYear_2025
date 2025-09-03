def matrix_dimensions(matrix):
    if not matrix:
        return (0, 0)
    return (len(matrix), len(matrix[0]))
