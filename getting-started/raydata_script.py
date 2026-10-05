
# Credit: Zachary Huang: https://www.youtube.com/watch?v=4Rbd_1Kb2qU&t=107s

import ray

ray.init(address="auto")

import numpy as np

def process_image(image_row : dict):
    image = image_row['image']
    processed_image = 255 - image
    return {"processed_image": processed_image}

print("Creating ds reference")
ds = ray.data.read_images("gs://imput-bucket/images")

print("Defining map transformations")
processed_ds = ds.map(process_image)

print("Lazy execution")
processed_ds.write_images(
    "gs://output-bucket/images",
    column="processed_image",
    try_create_dir=False,
)
