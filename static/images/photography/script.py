#!/usr/bin/env python3

from os import listdir, remove, rename
from os.path import isfile, join
# from os import path

import pprint


image_path = "mandalpatti-2017"

images = [f for f in listdir(image_path) if isfile(join(image_path, f))]


def get_image_width(image):
    parts = image.split("__")
    image_width = parts[1].split(".")[0].split("x")[0]
    return int(image_width)


'''

{
    "image_group_1" : {
        "width_1": "image_1",
    }
}
'''
image_groups = {}

for image in images:
    parts = image.split("__")
    image_width = int(parts[1].split(".")[0].split("x")[0])
    image_name = parts[0]

    if image_name not in image_groups:
        image_groups[image_name] = {}
        image_groups[image_name][image_width] = image
    
    if image.startswith(image_name):
        image_groups[image_name][image_width] = image
    
# pprint.pprint(image_groups)

to_delete = []
    
for image_group in image_groups.keys():

    biggest_image_width = max(image_groups[image_group].keys())
    smallest_image_width = min(image_groups[image_group].keys())


    biggest_image = join(image_path, image_groups[image_group][biggest_image_width])
    smallest_image = join(image_path, image_groups[image_group][smallest_image_width])

    # print(smallest_image)

    biggest_image_new_name = join(image_path, image_group + ".jpg")
    smallest_image_new_name = join(image_path, image_group + "-thumb.jpg")

    print("-----")
    rename(biggest_image, biggest_image_new_name)
    rename(smallest_image, smallest_image_new_name)
    print(biggest_image_new_name)
    print(smallest_image_new_name)
    print("-----")



    # Delete the non biggest and non-smallest images
    for image_width in image_groups[image_group]:
        if image_width != biggest_image_width and image_width != smallest_image_width:
            to_delete.append(image_groups[image_group][image_width])


# for image in to_delete:
#     full_path = join(image_path, image)
#     print("Deleting : ", full_path)
#     remove(full_path)