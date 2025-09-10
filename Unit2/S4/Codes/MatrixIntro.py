# Create a 3x3 matrix filled with zeros
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

matrix[0][1] = 6
matrix[2][2] = matrix[0][1] + matrix[0][1]

print("Initial Matrix:")
for row in matrix:
    print(row)


# Update element at row 1, column 2
matrix[0][1] = 5

# Update the element at row 3, column 3?
matrix[2][2] = 9

print("\nMatrix After Updates:")
for row in matrix:
    print(row)

for i in range(len(matrix)):
 for j in range(len(matrix[i])) :
   matrix[i][j] =    matrix[i][j] + 5

print("\nMatrix After all the element Updates:")
for row in matrix:
    print(row)


for i in range(len(matrix)):
   matrix[i][i] =    matrix[i][i] + 6

#secondary diagonal
for i in range(len(matrix)):
   matrix[i][n-i-1] =    matrix[i][n-i-1] + 10

