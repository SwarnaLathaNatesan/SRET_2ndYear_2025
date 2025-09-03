def identity_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append([1 if i == j else 0 for j in range(n)])
    return matrix
