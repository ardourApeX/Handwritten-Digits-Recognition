import numpy as np
import cv2 as cv
x_record = 0
y_record = 0
is_drawing = False
image = np.ones((512, 512, 3), np.uint8) * 1 # Black drawing board

# This is to get the coordinates to crop the image
x_min, x_max, y_min, y_max = 1000, 0, 1000, 0

def event_listener(event, x, y, flags, param):

	global x_record, y_record, is_drawing, x_max, x_min, y_max, y_min

	if event == cv.EVENT_LBUTTONDOWN:
		'''It is to detect left click : Starting Point of Gesture'''
		
		is_drawing = True # Now as we have drawn something on canvas
		x_record, y_record = x, y
		x_max = max(x_max, x_record)
		x_min = min(x_min, x_record)

		y_max = max(y_max, y_record)
		y_min = min(y_min, y_record)
		cv.imshow("image", image)

	elif event == cv.EVENT_MOUSEMOVE and is_drawing == True:
		'''It keeps track of mouse till drawing'''

		cv.line(image, (x_record, y_record), (x, y), (0, 255, 255), 10) #x y are dynamic variables
		
		x_record, y_record = x, y
		x_max = max(x_max, x_record)
		x_min = min(x_min, x_record)

		y_min = min(y_min, y_record)
		y_max = max(y_max, y_record)

		cv.imshow("image", image)

	elif event == cv.EVENT_LBUTTONUP:
		is_drawing = False # Drawing completed
		cv.line(image, (x_record, y_record), (x, y), (0, 255, 255), 10)
		cv.imshow("image", image)


cv.imshow('image', image)

cv.setMouseCallback('image', event_listener)
cv.waitKey(0)

roi_image = image[y_min : y_max, x_min : x_max, : ]
cv.imshow("Cropped",roi_image)

cv.waitKey(0)
cv.destroyAllWindows()