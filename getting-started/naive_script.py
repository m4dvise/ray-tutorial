
# Credit: Zachary Huang: https://www.youtube.com/watch?v=4Rbd_1Kb2qU&t=107s

import numpy as np
import time

def process_image(image : np.ndarray) -> np.ndarray:
    time.sleep(1)
    return 255 - image

images = [ np.random.randint(0, 255, (10, 10, 3)) for _ in range(8) ]

start_time = time.time()

result = [ process_image(image) for image in images ]

end_time = time.time()

print(f"Processed 8 iamges in time {(end_time - start_time):.2f}")
