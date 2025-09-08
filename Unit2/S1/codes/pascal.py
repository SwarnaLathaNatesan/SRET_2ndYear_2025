def generate_pascals_triangle(rows):
    triangle = [[1]]  # Initialize the triangle with the first row

    for row in range(1, rows):
        prev_row = triangle[-1]
        new_row = [1]  # First element is always 1
        for col in range(1, row):
	    newElement = prev_row[col] +prev_row[col - 1]
            new_row.append(newElement)
        new_row.append(1)  # Last element is always 1
        triangle.append(new_row)
    return triangle

# Example: Display Pascal's Triangle
rows = 5
triangle = generate_pascals_triangle(rows)
for r in triangle:
    print(r)
