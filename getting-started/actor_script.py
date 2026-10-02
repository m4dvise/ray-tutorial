
# Credit: Zachary Huang: https://www.youtube.com/watch?v=4Rbd_1Kb2qU&t=107s
import ray

ray.init()

import numpy as np
import time


@ray.remote
class PixelCounter:
    def __init__(self):
        self.total_pixel = 0

    def add(self, image : np.ndarray):
        self.total_pixel += image.size
    
    def get_total(self) -> int:
        return self.total_pixel


@ray.remote
def process_image(image : np.ndarray, counter : "ActorHandle") -> np.ndarray:
    counter.add.remote(image)
    time.sleep(1)
    return 255 - image

counter = PixelCounter.remote()

images = [ np.random.randint(0, 255, (10, 10, 3)) for _ in range(8) ]

start_time = time.time()

result_refs = [ process_image.remote(image, counter) for image in images ]
result = ray.get(result_refs)

total_pixels = ray.get(counter.get_total.remote())

end_time = time.time()

print(f"Processed {len(images)} images in time {(end_time - start_time):.2f}")
print(f"Pixel count : {total_pixels}")
