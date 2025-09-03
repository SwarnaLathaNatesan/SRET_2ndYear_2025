def rotate_180(matrix):
    result = []
    for row in reversed(matrix):
        result.append(list(reversed(row)))
    return result
