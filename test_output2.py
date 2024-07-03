import threading
import timeit
threads = []
threads_num = 4
filename = 'example.txt'

start_time = timeit.timeit()
                 
def thread_func(i):
    with open(filename, 'a') as file:
        file.write(f"This is line{i}.\n")


# Creating threads
for i in range(100):
    thread = threading.Thread(target=thread_func, args=([i]))
    threads.append(thread)

# Starting threads
for thread in threads:
    thread.start()

# Wait for threads to finish
for thread in threads:
    thread.join()
    
end_time = timeit.timeit()

print(f"elapsed time : {end_time - start_time}")
        