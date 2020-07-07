#Function Code

#Import the Needed Libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2

#wrapper around the imshow - for testing
def display_img(string,image):
    cv2.imshow(string,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def edge_detection(image):
    hsvImage = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #bgr to hsv
    lowerArray = np.array([60,40,40])
    upperArray = np.array([150,255,255])
    maskedImg = cv2.inRange(hsvImage,lowerArray,upperArray) #blue mask
    edges = cv2.Canny(maskedImg,200,400) #edge detection
    return edges

def crop_image(image):
    height, width = image.shape
    mask = np.zeros_like(image)
    region = np.array([[(0, height * 1 / 2),(width, height * 1 / 2),
        (width, height),
        (0, height),
    ]], np.int32)

    cv2.fillPoly(mask,region,255)
    cropped = cv2.bitwise_and(edges,mask) #want to bit-mask to hide this
    return cropped

# Code for Testing Images
frame = cv2.imread('E:\CVFolower\Capture.PNG')
edges = crop_image(edge_detection(frame))
display_img('cropped-edges',edges)
