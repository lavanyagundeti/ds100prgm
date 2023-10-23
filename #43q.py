#43q


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


rows = len(matrix)
cols = len(matrix[0])


transpose = []


for j in range(cols):
   
    new_row = []
    for i in range(rows):
        
        new_row.append(matrix[i][j])
    transpose.append(new_row)


print("Original Matrix:")
for row in matrix:
    print(row)


print("\nTranspose:")
for row in transpose:
    print(row)
