import os
import time
from PIL import Image, ImageFilter
from multiprocessing import Pool


IMAGES_LOC = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Images")
IMAGES_DEST = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Processed")

if not os.path.exists(IMAGES_DEST):
    try:
        os.mkdir(IMAGES_DEST)
    except OSError as e:
        print(e)

images_locations = [f"{IMAGES_LOC}\\{image_loc}" for image_loc in os.listdir(IMAGES_LOC)]


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
            result = pool_executor.apply_async(process_image, args=(image_loc,))
            result.wait()
            print("Ended processing")
    t3 = time.perf_counter()
    print(t3 - t2)

