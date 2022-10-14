import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("noisy/cat.jpeg")
sharpenMatrix= ([[0,-1,0],
				[-1,5,-1],
				[0,-1,0]])
sharpenNP=np.array(sharpenMatrix)
kernel = np.ones((3,3), np.float32)/9

size=3

def medianBlur(img):
	return cv2.medianBlur(img,size)

def gaussianBlur(img):
	return cv2.GaussianBlur(img,(size,size),0)

def bilateral(img):
	return cv2.bilateralFilter(img,9,75,75)

def blur(img):
	return cv2.blur(img,(size,size))

def convolution(img,kernel):
	return cv2.filter2D(img,-1,kernel)

def waiter():
	cv2.waitKey(0);
	cv2.destroyAllWindows()


if __name__ == '__main__':

	cv2.imshow("Goc", img)
	cv2.imshow("medianBlur", medianBlur(img))
	cv2.imshow("gaussianBlur", gaussianBlur(img))
	cv2.imshow("bilateral", bilateral(img))
	cv2.imshow("blur", blur(img))
	cv2.imshow("filterCustomBlur", convolution(img,kernel))



	waiter()

