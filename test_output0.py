import threading
import timeit
threads = []
threads_num = 4
import math
# Function definition
def compute_factorial(n):
    result = math.factorial(n)
    print(f"Factorial of {n} is {result}")

numbers = [5, 7, 10, 12, 15, 18, 20, 25, 30, 35]
start_time = timeit.timeit()

for number in numbers:
   
    # Creating threads                 
    thread = threading.Thread(target=compute_factorial, args=[number])
    threads.append(thread)

# Starting threads  
for thread in threads:
    thread.start()
    
# Wait for threads to finish
for thread in threads:
    thread.join()

end_time = timeit.timeit()
print(f"elapsed time : {end_time - start_time}")
        