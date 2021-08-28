import requests
import os
import random
import string
import shutil


"""
A script that takes the target image_url and fills the directory with the chosen image all with randomly named copys

"""

image_url = ""  # image to be downloaded
init_image = "$Howdy"  # Message at the top of directory
image_count = 5 # How many images to be put in the directory


def pull_image(url, name):
    try:
        with open(name, 'wb') as file:
            file.write(requests.get(url).content)
            file.close()
    except Exception as e:
        print(f"Error was caught: {e}")
    return name


def randletter(x, y):
    return chr(random.randint(ord(x), ord(y)))


def gen_name():
    name_len = random.randint(3, 30)
    random_letter = ""
    for i in range(name_len):
        random_letter += randletter('a','z')
    return random_letter + '.jpg'


def cheeky(cpy_file):
    try:
        shutil.copyfile(cpy_file, gen_name())
    except Exception as e:
        print(f'error copying file: {e}')

# copy_file = pull_image(image_url)
imageName = pull_image(image_url, init_image+'.jpg')
if image_count >= 50:
    print(f"Nah {image_count} images is too many, thats rather cheeky")
    quit()
else:
    for i in range(image_count):
        cheeky(imageName)
