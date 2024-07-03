import threading
import timeit
threads = []
threads_num = 4

def print_numbers(file):
    for i in range(len(file)):
        print(file[i])

files = []

start_time = timeit.timeit()

for file in files:
                    
    thread = threading.Thread(target=print_numbers, args=(file))
    threads.append(thread)
    
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

end_time = timeit.timeit()
print(f"elapsed time : {end_time - start_time}")
        
