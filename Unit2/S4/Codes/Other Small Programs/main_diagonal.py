def main_diagonal(matrix):
    diagonal = []
    for i in range(min(len(matrix), len(matrix[0]))):
        diagonal.append(matrix[i][i])
    return diagonal
