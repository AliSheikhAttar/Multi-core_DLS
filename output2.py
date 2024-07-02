import threading

def thread_func(i):
    print(i, i*100)
    print(i, i*100)
    print(i, i*100)


threads = []

for i in range(50):
    thread = threading.Thread(target=thread_func, args=(i))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()