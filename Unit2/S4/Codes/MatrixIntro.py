# Create a 3x3 matrix filled with zeros
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

print("Initial Matrix:")
for row in matrix:
    print(row)


# Update element at row 1, column 2
matrix[0][1] = 5

# Update the element at row 0, column 0
#matrix = 9

print("\nMatrix After Updates:")
for row in matrix:
    print(row)

