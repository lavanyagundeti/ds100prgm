#48q


import numpy as np


matrix = np.array([
    [2, 5, 3],
    [1, 7, 4],
    [8, 6, 9]
])

determinant = np.linalg.det(matrix)

print("Matrix:")
print(matrix)
print(f"Determinant: {determinant:.2f}")
