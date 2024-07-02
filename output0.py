import threading
def print_numbers(start, end):
    for i in range(start, end + 1):
        print(i)


end = 20
start = 10
num_threads = 10
threads = []
step = int((end - start)/ 10)

for i in range(start,end,step):
    thread = threading.Thread(target=print_numbers, args=(i, i+step))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

