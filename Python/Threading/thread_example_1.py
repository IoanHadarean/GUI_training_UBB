import time
from threading import Thread

list_of_files = ["thread_example_1.txt", "thread_example_2.txt"]


print("Started...")


def write_data_to_file(file):
    time.sleep(1)
    try:
        with open(file, "w", encoding="utf-8") as write_file:
            write_file.write("This is a new line.")
    except OSError as e:
        print(e)
    finally:
        print("Success.")


start = time.perf_counter()
threads = []

# for data_file in list_of_files:
#     write_data_to_file(data_file)
for data_file in list_of_files:
    thread = Thread(target=write_data_to_file, args=(data_file,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

stop = time.perf_counter()
print(f"Finished in {round(stop - start, 4)} seconds.")


