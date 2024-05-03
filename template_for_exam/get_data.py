import os


def get_data():
    """returns []{img: str, mask: str}"""
    imgs = os.listdir("data/images")
    data = []
    for img in imgs:
        x = img.split(".")
        x.insert(1, "_mask.")
        mask = "".join(x)
        data.append({"img": img, "mask": mask})
    return data
