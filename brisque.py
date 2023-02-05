# !pip install image-quality
import imquality.brisque as brisque
import PIL.Image
import argparse
import imutils
import warnings
warnings.filterwarnings('ignore')

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="220310_images\\original.png")
args = vars(ap.parse_args())

img = PIL.Image.open(args["image"]).convert('L')

print('BRISQUE: {}'.format(brisque.score(img)))