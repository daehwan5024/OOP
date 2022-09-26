import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
img = Image.open('gslogo.jpg')
print(img)
array = np.array(img)
plt.imshow(255 - array)
plt.show()
