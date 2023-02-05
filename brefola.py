import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="220310_images\\original.png")
args = vars(ap.parse_args())

img = cv2.imread(args["image"], cv2.IMREAD_GRAYSCALE) # read as gray scale
resized_img = cv2.resize(img, dsize=(1920, 1080), interpolation=cv2.INTER_LINEAR)

f = np.fft.fft2(resized_img) # FFT
fshift = np.fft.fftshift(f) # Shift the center of the spectrum
magnitude_spectrum = 14*np.log(1+np.abs(fshift)) # Log transform

white_area = np.zeros(shape=(1080,1920))
white_area[magnitude_spectrum > 100] = 1

values = white_area.sum()
        
canny_edge = cv2.Laplacian(resized_img, cv2.CV_8U,ksize=3)
ic = canny_edge.sum()

brefola = values / np.sqrt(ic) / 5 # Scaling to have values between 0 and 100

if brefola > 100:
    brefola = 100
elif brefola < 0:
    brefola = 0

print('BREFOLA: {}'.format(brefola))
    

