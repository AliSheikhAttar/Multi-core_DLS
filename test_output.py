#########################################
import threading

# Define a function for the thread
def print_numbers(start, end):
    for i in range(start, end + 1):
        print(i)

# Create threads
thread1 = threading.Thread(target=print_numbers, args=(1, 5))
thread2 = threading.Thread(target=print_numbers, args=(6, 10))

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()