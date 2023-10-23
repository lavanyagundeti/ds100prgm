#47q

def extract_submatrix(matrix, start_row, end_row, start_col, end_col):
    submatrix = []
    for i in range(start_row, end_row + 1):
        row = matrix[i][start_col:end_col + 1]
        submatrix.append(row)
    return submatrix


larger_matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]


start_row = 1
end_row = 2
start_col = 1
end_col = 2


submatrix = extract_submatrix(larger_matrix, start_row, end_row, start_col, end_col)


print("Original Matrix:")
for row in larger_matrix:
    print(row)

print("\nExtracted Submatrix:")
for row in submatrix:
    print(row)
