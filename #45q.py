#45q

def main_diagonal_sum(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("The input matrix must be square for the main diagonal sum.")

    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]

    return diagonal_sum

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


sum_diagonal = main_diagonal_sum(matrix)


print("Original Matrix:")
for row in matrix:
    print(row)

print(f"\nSum of the Main Diagonal: {sum_diagonal}")
