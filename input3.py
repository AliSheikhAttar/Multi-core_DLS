import random

def matrix_multiply(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    print("multiply of two matrices are: {}\n".format(result))

def matrix_sum(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]

    print("sum of two matrices are: {}\n".format(result))

def matrix_dot_product(A, B):
    n = len(A)
    result = 0
    for i in range(n):
        for j in range(n):
            result += A[i][j] * B[i][j]

    print("Dot product of two matrices are: {}\n".format(result))




n = 8
A = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
B = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]


print("Matrix A:")
for row in A:
    print(row)
print("Matrix B:")
for row in B:
    print(row)

result_multiply = matrix_multiply(A, B)
result_sum = matrix_sum(A, B)
result_dot_product = matrix_dot_product(A, B)

