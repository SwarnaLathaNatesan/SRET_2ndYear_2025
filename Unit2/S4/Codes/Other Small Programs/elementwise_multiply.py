def elementwise_multiply(A, B):
    result = []
    for i in range(len(A)):
        result.append([A[i][j] * B[i][j] for j in range(len(A[0]))])
    return result
