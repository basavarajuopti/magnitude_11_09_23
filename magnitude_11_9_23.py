import cv2
import numpy as np
import matplotlib.pyplot as plt
from time import time
def get_magnitude(img):
    st = time()
    gx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    gy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = np.sqrt(gx**2 + gy**2)
    et = time()
    print(f'Time taken for calculating magnitude {et-st} seconds')
    return magnitude
img_path = 'C:\\Users\\Lenovo\\Desktop\\a\\b\\11.jpeg'
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
magnitude = get_magnitude(img)
plt.figure()
plt.imshow(magnitude,cmap='gray')
plt.show()