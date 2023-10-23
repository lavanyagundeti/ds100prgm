#46q

def matrix_addition(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    
    result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[i][j] + B[i][j]

    return result

def matrix_subtraction(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions for subtraction.")
    
    result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[i][j] - B[i][j]

    return result


A = [
    [1, 2, 3],
    [4, 5, 6],
]

B = [
    [7, 8, 9],
    [10, 11, 12],
]


result_addition = matrix_addition(A, B)

result_subtraction = matrix_subtraction(A, B)

print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nMatrix A + B:")
for row in result_addition:
    print(row)

print("\nMatrix A - B:")
for row in result_subtraction:
    print(row)
