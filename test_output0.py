import threading
threads = []
threads_num = 4

def print_numbers(start, end):
    for i in range(start, end + 1):
        print(i)




sep =  end - start + 1
for t in range(threads_num):
    thread = threading.Thread(target=print_numbers, args=(t*(sep/threads_num), (t + 1)*(sep/threads_num)))
    threads.append(thread)
for thread in threads:
    thread.start()
for thread in threads:
   thread.join()
