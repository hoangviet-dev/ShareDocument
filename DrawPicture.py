import numpy as np
import matplotlib.pyplot as plt
import time

image = np.full((100, 255), 0)

for i in range(0, 255):
    image[0:100, i:(i+1)] = i

# chu K
for i in range(20, 25):
    image[15:95, i] = 256 - i

for j in range(40, 50):
    for i in range(25, 50):
        image[(j - (i - 25)), i] = 256 - i

plt.imshow(image)
plt.show()
