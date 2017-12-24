import cv2
from PIL import Image
import numpy as np
import time

# mask image path
maskPath = "/home/reshu/Desktop/fsoc.png"
# haarcascade path
cascPath = "/home/reshu/opencv/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_default.xml"

# cascade classifier object 
faceCascade = cv2.CascadeClassifier(cascPath)

# Open mask as PIL image
mask = Image.open(maskPath)

def fsoc_mask(image):
	"""
	function to add mask to input image
	"""

	# convert input image to grayscale
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# detect faces in grayscale image
	faces = faceCascade.detectMultiScale(gray, 1.15)

	# convert cv2 imageto PIL image
	background = Image.fromarray(image)

	for (x,y,w,h) in faces:
		# resize mask
		resized_mask = mask.resize((w,h), Image.ANTIALIAS)
		# define offset for mask
		offset = (x,y)
		# pask mask on background
		background.paste(resized_mask, offset, mask=resized_mask)

	# return background as cv2 image
	return np.asarray(background)

# VideoCapture object
cap = cv2.VideoCapture(cv2.CAP_ANY)

while True:
	# read return value and frame
	ret, frame = cap.read()

	if ret == True:
		# show frame with thug life mask
		cv2.imshow('Live', fsoc_mask(frame))

		# chck if esc key is pressed
		if cv2.waitKey(1) == 27:
			break

# release cam
cap.release()
# destroy all open opencv windows
cv2.destroyAllWindows()
