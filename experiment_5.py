"""
Experiment No 5. Develop a program to apply DCT on a gray level image 16X16 and
plot the transformed image. Then apply IDCT on the transformed image and plot it also.
"""

import numpy as np
import matplotlib.pyplot as plt

# define a function to perform DCT on an image
def dct(image):
    height, width = image.shape
    dct_image = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            sum = 0
            for x in range(height):
                for y in range(width):
                    sum += image[x][y] * np.cos(np.pi * (2 * x + 1) * i / (2 * height)) * np.cos(np.pi * (2 * y + 1) * j / (2 * width))
            sum *= 2 / np.sqrt(height * width)
            if i == 0:
                sum *= 1 / np.sqrt(2)
            if j == 0:
                sum *= 1 / np.sqrt(2)
            dct_image[i][j] = sum

    return dct_image

# define a function to perform IDCT on an image
def idct(dct_image):
    height, width = dct_image.shape
    image = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            sum = 0
            for x in range(height):
                for y in range(width):
                    coeff = 1
                    if x == 0:
                        coeff *= 1 / np.sqrt(2)
                    if y == 0:
                        coeff *= 1 / np.sqrt(2)
                    sum += coeff * dct_image[x][y] * np.cos(np.pi * (2 * i + 1) * x / (2 * height)) * np.cos(np.pi * (2 * j + 1) * y / (2 * width))
            sum *= 2 / np.sqrt(height * width)
            image[i][j] = sum

    return image

# create a random gray level image of size 16x16
image = np.random.randint(0, 256, size=(16, 16))

# plot the original image
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

# perform DCT on the image
dct_image = dct(image)

# plot the transformed image
plt.subplot(1, 3, 2)
plt.imshow(dct_image, cmap='gray')
plt.title('Transformed Image')

# perform IDCT on the transformed image
reconstructed_image = idct(dct_image)

# plot the reconstructed image
plt.subplot(1, 3, 3)
plt.imshow(reconstructed_image, cmap='gray')
plt.title('Reconstructed Image')

plt.show()
