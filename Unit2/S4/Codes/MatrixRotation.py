#Python code for matrix rotation
def rotate_clockwise(matrix):
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    
    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    




    return matrix

# Example usage
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
rotated = rotate_clockwise(matrix)
for row in rotated:
    print(row)
            
