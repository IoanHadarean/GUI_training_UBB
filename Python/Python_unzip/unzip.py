import os
import zipfile
import logging
from filecmp import cmp

DESKTOP_PATH = r"C:\Users\hadarean\Desktop"
ZIP_FILES_PATH = os.path.join(DESKTOP_PATH, "zip_files.zip")
UNZIP_FILES_PATH = os.path.join(DESKTOP_PATH, "unzipped_files")

files_to_zip = []

for entry in os.listdir(DESKTOP_PATH):
    print(entry)
    file_path = os.path.join(DESKTOP_PATH, entry)
    if "yaml" in entry and not os.path.isdir(file_path):
        files_to_zip.append(file_path)
    print(file_path)
    print(os.path.abspath(entry))
    print(os.path.realpath(entry))
    print(os.path.relpath(file_path))

for root, dirs, files in os.walk(DESKTOP_PATH, topdown=False):
    for name in files:
        if "yaml" in name:
            files_to_zip.append(os.path.join(root, name))
            print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))


def remove_duplicate_files(no_duplicate_files=None):
    files_to_zip_dirs = [os.path.dirname(file_path) for file_path in files_to_zip]
    print(files_to_zip_dirs)
    files_to_zip_basenames = [os.path.basename(file_path) for file_path in files_to_zip]
    print(files_to_zip_basenames)
    basenames = []
    for idx in range(len(files_to_zip_dirs)):
        current_dir = files_to_zip_dirs[idx]
        current_file = files_to_zip_basenames[idx]
        if current_file in basenames:
            continue
        else:
            basenames.append(current_file)
            no_duplicate_files.append(os.path.join(current_dir, current_file))
    return no_duplicate_files


def zip_files():
    no_duplicate_files = remove_duplicate_files([])
    with zipfile.ZipFile(ZIP_FILES_PATH, 'w') as zip_dir:
        for file_path in no_duplicate_files:
            zip_dir.write(file_path, os.path.basename(file_path))


def unzip_files():
    try:
        os.mkdir(UNZIP_FILES_PATH)
    except OSError:
        logging.info(f"Failed to create folder {UNZIP_FILES_PATH}")

    with zipfile.ZipFile(ZIP_FILES_PATH, "r") as zip_ref:
        zip_ref.extractall(UNZIP_FILES_PATH)


zip_files()
unzip_files()



