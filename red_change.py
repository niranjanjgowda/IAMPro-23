import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imshow, imread
from skimage.color import rgb2hsv, hsv2rgb
import cv2

red = imread('picturetest.png')
plt.figure(num=None, figsize=(8, 6), dpi=80)
