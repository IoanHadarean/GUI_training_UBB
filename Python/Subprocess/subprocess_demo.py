import os
import subprocess

FOLDER_PATH = os.path.dirname(os.path.realpath(__file__))

FOLDER_A_LOC = f"{FOLDER_PATH}\\Folder A"
FOLDER_B_LOC = f"{FOLDER_PATH}\\Folder B"
try:
    os.mkdir(FOLDER_A_LOC)
except OSError as e:
    print(e)

list_of_folders = [(f"FOLDER_{idx}", f"FOLDER_{idx}.txt") for idx in range(10)]
print()

for folder in list_of_folders:
    folder_name, folder_file = folder

    folder_destination = f"{FOLDER_A_LOC}\\{folder_name}"
    if not os.path.exists(folder_destination):
        try:
            os.mkdir(folder_destination)
        except OSError as e:
            print(e)

    with open(f"{folder_destination}\\{folder_file}", "w", encoding="utf-8") as folder_file:
        folder_file.write("This is a log.")
        folder_file.close()

process = subprocess.Popen(['robocopy', f"{FOLDER_A_LOC}", f"{FOLDER_B_LOC}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(process.pid)
stdout, stderr = process.communicate()
process.terminate()
print(stdout, stderr)

with open(f"{FOLDER_A_LOC}\\logs.txt", "w", encoding="utf-8") as logs_file:
    logs_file.write(stdout.decode(encoding="utf-8"))
    logs_file.close()

process_task_kill = subprocess.run(['taskkill', '/IM', 'msedge.exe', '/F'])
print(process_task_kill.returncode)