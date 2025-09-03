def scalar_multiply(matrix, scalar):
    result = []
    for row in matrix:
        result.append([element * scalar for element in row])
    return result
