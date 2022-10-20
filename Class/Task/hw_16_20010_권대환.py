from skimage.exposure import rescale_intensity
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def convolve(image, kernel):
    (iH, iW) = image.shape
    (kH, kW) = kernel.shape
    pad = int((kH-1)/2)

    pad_image = np.zeros((iW + pad*2, iH + pad*2))
    pad_image[pad:-pad, pad:-pad] = image
    pad_image[:pad, :pad] = np.full((pad, pad), image[0, 0])
    pad_image[-pad:, :pad] = np.full((pad, pad), image[-1, 0])
    pad_image[-pad:, -pad:] = np.full((pad, pad), image[-1, -1])
    pad_image[:pad, -pad:] = np.full((pad, pad), image[0, -1])
    pad_image[:pad, pad:-pad] = image[0, :]
    pad_image[-pad, pad:-pad] = image[-1, :]
    pad_image[pad:-pad, :pad] = image[:, 0].reshape(256, 1)
    pad_image[pad:-pad, -pad:] = image[:, -1].reshape(256, 1)
    output_image = np.zeros((iH, iW))

    for y in np.arange(iH):
        for x in np.arange(iW):
            roi = pad_image[x:x+kW, y:y+kH]
            k = (roi * kernel).sum()
            output_image[x, y] = k

    output_image = rescale_intensity(output_image, in_range=(0, 255))
    new_image = (output_image * 255).astype("uint8")
    return new_image


original = np.array((
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]), dtype="int")

sharpen = np.array((
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]), dtype="int")

smallBlur = np.full((7, 7), 1/49)

laplacian = np.array((
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]), dtype="int")

sobelX = np.array((
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]), dtype="int")

sobelY = np.array((
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]), dtype="int")

kernelBank = (
    ('original', original), ('sharpen', sharpen), ('smallBlur', smallBlur),
    ('laplacian', laplacian), ('sobelX', sobelX), ('sobleY', sobelY)
)

image = Image.open("test2.jpg").convert("L")
image = np.array(image)

fig = plt.figure()

for i, filter in enumerate(kernelBank):
    ax = fig.add_subplot(2, 3, i+1)
    convolveOutput = convolve(image, filter[1])
    ax.set_title(filter[0])
    ax.imshow(convolveOutput, cmap="gray")

plt.show()
