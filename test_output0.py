import threading
import timeit
threads = []
threads_num = 4

def print_numbers(start, end):
    for i in range(start, end + 1):
        print(i)

end = 100
start = 0
step = 25

start_time = timeit.timeit()

for i in range(start, end, step):
    thread = threading.Thread(target=print_numbers, args=(i, i+step))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time = timeit.timeit()
print(f"elapsed time : {start_time - end_time}")
                        