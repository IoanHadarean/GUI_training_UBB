import threading
from threading import Thread

x = 0


def increment_variable():
    global x
    for i in range(450000):
        x += 1
# def increment_variable(thread_lock):
#     global x
#     thread_lock.acquire()
#     for i in range(10000000):
#         x += 1
#     thread_lock.release()


threads = []
for idx in range(2):

    thread = Thread(target=increment_variable)
    thread.start()
    threads.append(thread)
# lock = threading.Lock()
# for idx in range(2):
#
#     thread = Thread(target=increment_variable, args=(lock,))
#     thread.start()
#     threads.append(thread)


for thread in threads:
    thread.join()

print(x)
