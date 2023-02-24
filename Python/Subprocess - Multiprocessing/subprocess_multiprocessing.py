import os
import subprocess
import time
from subprocess import PIPE
from PIL import Image, ImageFilter
from multiprocessing import Pool

FOLDER_PATH = "C:\\Users\\hadarean\\Desktop"

FOLDER_A_LOC = f"{FOLDER_PATH}\\Folder A"
FOLDER_B_LOC = f"{FOLDER_PATH}\\Folder B"
try:
    os.mkdir(FOLDER_A_LOC)
except OSError as e:
    print(e)
IMAGES_LOC = r"C:\Users\hadarean\Desktop\Images"
IMAGES_DEST = r"C:\Users\hadarean\Desktop\Processed"

process = subprocess.Popen(['robocopy', f"{FOLDER_A_LOC}", f"{FOLDER_B_LOC}"], stdout=PIPE, stderr=PIPE)
print(process.pid)
stdout, stderr = process.communicate()
process.terminate()
print(stdout, stderr)

with open(f"{FOLDER_A_LOC}\\logs.txt", "w", encoding="utf-8") as logs_file:
    logs_file.write(stdout.decode(encoding="utf-8"))
    logs_file.close()
#

process_task_kill = subprocess.run(['taskkill', '/IM', 'msedge.exe', '/F'])
print(process_task_kill.returncode)


list_of_folders = [(f"FOLDER_{idx}", f"FOLDER_{idx}.txt") for idx in range(10)]
print()

for folder in list_of_folders:
    folder_name, folder_file = folder

    folder_destination = f"{FOLDER_PATH}\\{folder_name}"
    if not os.path.exists(folder_destination):
        try:
            os.mkdir(folder_destination)
        except OSError as e:
            print(e)

    with open(f"{folder_destination}\\{folder_file}", "w", encoding="utf-8") as folder_file:
        folder_file.write("This is a log.")
        folder_file.close()

images_locations = [f"{IMAGES_LOC}\\{image_loc}" for image_loc in os.listdir(IMAGES_LOC)]
print()


def process_image(image_loc):
    print("Started processing")
    image = Image.open(image_loc)
    image = image.filter(ImageFilter.GaussianBlur(15))
    image.thumbnail((1200, 1200))
    image.save(f"{IMAGES_DEST}\\{os.path.basename(image_loc)}")
    print("Ended processing")


if __name__ == "__main__":
    # t1 = time.perf_counter()
    # for image_loc in images_locations:
    #     process_image(image_loc)
    t2 = time.perf_counter()
    # print(t2 - t1)
    with Pool(processes=1) as pool_executor:
        for image_loc in images_locations:
            print("Started processing")
            pool_executor.apply_async(process_image, args=(image_loc,))
            print("Ended processing")
    t3 = time.perf_counter()
    print(t3 - t2)

