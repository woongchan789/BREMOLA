from skimage.metrics import structural_similarity as ssim 
from skimage import io
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--original", required=True, help="220310_images\\original.png") 
ap.add_argument("-d", "--distortion", required=True, help="220310_images\\145_2h.png")
args = vars(ap.parse_args())

imageA = cv2.imread(args["original"])
imageB = cv2.imread(args["distortion"])

grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

(score, diff) = ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")

print("SSIM: {}".format(score))