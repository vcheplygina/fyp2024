
import os
import shutil

filename = "image_ids_groups.csv"

if filename not in os.listdir():
    raise Exception(f"Couldn't find the file with the ids called {filename}. Make sure to download it and put it in the same directory as this script.")

if "my_group_imgs" not in os.listdir():
    os.mkdir("my_group_imgs")

group_id = input("What is your group (assigned letter)? ")

with open("image_ids_groups.csv") as infile:

    for line in infile.readlines():

        id, d, group = line.strip().split(",")
        print(group)

        if group.upper() == group_id.upper():

            try:
                print(f"Copying file {id}")
                shutil.copy(id, f"my_group_imgs/{id}")
            except:
                print(f"WARNING: Couldn't copy file {id}.")
