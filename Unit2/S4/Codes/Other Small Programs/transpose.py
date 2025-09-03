def transpose(matrix):
    result = []
    for i in range(len(matrix[0])):
        result.append([matrix[j][i] for j in range(len(matrix))])
    return result
