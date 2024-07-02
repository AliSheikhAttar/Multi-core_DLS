import threading
def print_numbers(start, end):
    for i in range(start, end + 1):
        print(i)


threads = []

for i in range(50):
    print_numbers(i, i*100)
    thread = threading.Thread(target=print_numbers, args=(i, i*100))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
