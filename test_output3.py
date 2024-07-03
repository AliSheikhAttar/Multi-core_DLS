import threading
import timeit
threads = []
threads_num = 4

x = 4
x = 6

print("hello")
fsd = 4
def hello1():
    print("hello")
    x = 4*2
    print(x)

fsd = 4

def hello3():
    r = 4
    f = 3
fsd = 4
fsd = 4

def hello2(t):
    print("this")
    print("is")
    print(t)


r = 89
e = r*3
t = e/2

fsd = 4

fdsj = 9

start_time = timeit.timeit()


thread0 = threading.Thread(target=hello1,args=())

thread1 = threading.Thread(target=hello3,args=())

thread2 = threading.Thread(target=hello2,args=[t])

thread0.start()

thread1.start()

thread2.start()

thread0.join()

thread1.join()

thread2.join()


end_time = timeit.timeit()
print(f"elapsed time : {end_time - start_time}")
            