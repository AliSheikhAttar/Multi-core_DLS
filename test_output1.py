import threading
import timeit
threads = []
threads_num = 4

def print_numbers(start, end):
    for i in range(start, end + 1):
        print(i)



start_time = timeit.timeit()
for i in range(50):
                    
    thread = threading.Thread(target=print_numbers, args=(i, i*100))
    threads.append(thread)
    
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

end_time = timeit.timeit()
print(f"elapsed time : {end_time - start_time}")
        
