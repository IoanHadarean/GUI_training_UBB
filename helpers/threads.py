import time
from threading import Thread


def first_thread():
    time.sleep(10)
    print("First thread running\n")


def second_thread():
    time.sleep(10)
    print("Second thread running")


threads = [Thread(target=first_thread), Thread(target=second_thread)]

for thread in threads:
    thread.start()
    thread.join()

print("Hello")

