#########################################
import threading

# Define a function for the thread
def print_numbers(start, end):
    for i in range(start, end + 1):
        print(i)

threads = []
# Create threads
for i in range(n):
    thread = threading.Thread(target=print_numbers, args=(1, 5))
    threads.append(thread)
# Start threads
for thread in threads:
    thread.start()

# Wait for threads to complete
for thread in threads:
    thread.join()
