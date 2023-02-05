from math import log10, sqrt
import argparse
import imutils
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--original", required=True, help="220310_images\\original.png")
ap.add_argument("-d", "--distortion", required=True, help="220310_images\\145_2h.png")
args = vars(ap.parse_args())

imageA = cv2.imread(args["original"])
imageB = cv2.imread(args["distortion"])

mse = np.mean((imageA - imageB) ** 2)
if(mse == 0): 
    psnr = 100
max_pixel = 255.0
psnr = 20 * log10(max_pixel / sqrt(mse))

print('PSNR: {}'.format(psnr))