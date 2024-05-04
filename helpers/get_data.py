import os
from os.path import exists


def get_data():
    """returns []{img: str, mask: str}"""
    imgs = os.listdir("data/images")
    data = []
    for img in imgs:
        x = img.split(".")
        x.insert(1, "_mask.")
        mask = "".join(x)
        if exists(f"data/images/{img}") and exists(f"data/masks/{mask}"):
            data.append({"img": img, "mask": mask})
    return data
