
import numpy as np
import cv2
from matplotlib import pyplot as plt
import khuNhieu

img = cv2.imread("noisy/cat.jpeg")


def grayscale(img):
	return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_gray= grayscale(img)


img_blur = khuNhieu.medianBlur(img_gray) 


def sobelX(img):
	return cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)

def sobelY(img):
	return cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)

def sobelXY(img):
	return cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)

def canny(img):
	return cv2.Canny(image=img, threshold1=100, threshold2=200)

def waiter():
	cv2.waitKey(0);
	cv2.destroyAllWindows()


if __name__ == '__main__':

	cv2.imshow("Goc", img)
	cv2.imshow("sobelX", sobelX(img_blur))
	cv2.imshow("sobelY", sobelY(img_blur))
	cv2.imshow("sobelXY", sobelXY(img_blur))
	cv2.imshow("canny", canny(img_blur))



	waiter()

