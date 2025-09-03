def anti_diagonal(matrix):
    diagonal = []
    for i in range(len(matrix)):
        diagonal.append(matrix[i][len(matrix)-1-i])
    return diagonal
