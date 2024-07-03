import threading
import timeit
threads = []
threads_num = 4
import random

def matrix_multiply(A, B):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    print("multiply of two matrices are: {}\n".format(result))

def matrix_sum(A, B):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]

    print("sum of two matrices are: {}\n".format(result))

def matrix_dot_product(A, B):
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


start_time = timeit.timeit()


# Creating threads
thread0 = threading.Thread(target=matrix_multiply,args=(A, B))

thread1 = threading.Thread(target=matrix_sum,args=(A, B))

thread2 = threading.Thread(target=matrix_dot_product,args=(A, B))

# Starting threads
thread0.start()

thread1.start()

thread2.start()

# Wait for threads to finish
thread0.join()

thread1.join()

thread2.join()


end_time = timeit.timeit()
print(f"elapsed time : {end_time - start_time}")
            