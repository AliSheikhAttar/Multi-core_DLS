import threading
import timeit
threads = []
threads_num = 4
import math
def compute_factorial(start, end):
    for i in range(start, end):
        result = math.factorial(i)
        print(f"Factorial of {i} is {result}")


end =  10
start = 1
step = 2

start_time = timeit.timeit()

# Creating threads
for i in range(start, end, step):
    thread = threading.Thread(target=compute_factorial, args=(i, i+step))
    threads.append(thread)

# Starting threads 
for thread in threads:
    thread.start()

# Wait for threads to finish
for thread in threads:
    thread.join()

end_time = timeit.timeit()
print(f"elapsed time : {end_time - start_time}")
                        