
# Credit: Zachary Huang: https://www.youtube.com/watch?v=4Rbd_1Kb2qU&t=107s
import ray

ray.init()

import numpy as np
import time

@ray.remote
def process_image(image : np.ndarray) -> np.ndarray:
    time.sleep(1)
    return 255 - image

images = [ np.random.randint(0, 255, (10, 10, 3)) for _ in range(8) ]

start_time = time.time()

result_refs = [ process_image.remote(image) for image in images ]
result = ray.get(result_refs)

end_time = time.time()

print(f"Processed {len(images)} images in time {(end_time - start_time):.2f}")
