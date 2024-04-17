import cv2
from MotorController import MotorController
FOCAL_LENGTH = 3.6 / 25.4
OBJECT_1_KNOWN_WIDTH  = 0

def distance_to_camera(knownWidth, focalLength, perWidth):
	# compute and return the distance from the maker to the camera
	return (knownWidth * focalLength) / perWidth

