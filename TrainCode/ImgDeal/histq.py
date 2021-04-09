import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import random
img = cv.imread('temp.jpg',0)
def histPlot(img):
    hist,bins = np.histogram(img.flatten(),256,[0,256])
    cdf = hist.cumsum()
    cdf_normalized = cdf  * hist.max() / (cdf.max() - cdf.min())
    plt.plot(cdf_normalized, color = 'b')
    plt.hist(img.flatten(),256,[0,256], color = 'r')
    plt.xlim([0,256])
    plt.legend(('cdf','histogram'), loc = 'upper left')
    plt.show()

img2 = cv.imread('temp.jpg',0)
eq = cv.equalizeHist(img2)
res = np.hstack((img2,eq))
histPlot(img2)
histPlot(eq)
plt.imshow(res)
plt.show()
# cdf_m = np.ma.masked_equal(cdf,0)
# cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
# cdf = np.ma.filled(cdf_m,0).astype('uint8')
# image2 = cdf[img]
# plt.hist(img.flatten(),256,[0,256], color = 'r')
# plt.xlim([0,256])
# plt.legend(('cdf','histogram'), loc = 'upper left')
# plt.show()