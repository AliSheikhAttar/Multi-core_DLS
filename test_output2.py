import threading
import timeit
threads = []
threads_num = 4

start_time = timeit.timeit()
                 
def thread_func(i, j):
    print(i, i*100)
    x= i * i
    print(x)

for i in range(50):
    thread = threading.Thread(target=thread_func, args=[i, 0])
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
    
end_time = timeit.timeit()

print(f"elapsed time : {end_time - start_time}")
