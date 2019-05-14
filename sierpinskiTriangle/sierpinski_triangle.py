from numpy import *
from cv2 import *

#program creates sierpinski triangle from test image with set amout of iterations
#at some point image becomes completely white - size of elements is smaller than
#one pixel, so they are not shown
numberOfIterations = 5
for powtorzenia in range (0,numberOfIterations):
    img = cv2.imread("test.jpg")
    background = zeros((img.shape[0],img.shape[1],3), uint8)
    background[:,:] = (255,255,255)
    small = cv2.resize(img, (0,0), fx=0.333, fy=0.333)
    offsetY = [None]*6
    offsetX = [None]*6
    offsetY[0] = 0
    offsetX[0] = int(background.shape[1]/2)-int(small.shape[1]/2)
    offsetY[1] = small.shape[0]
    offsetX[1] = int(background.shape[1]/2)-int(small.shape[1])
    offsetY[2] = small.shape[0]
    offsetX[2] = int(background.shape[1]/2)
    offsetY[3] = 2*small.shape[0]
    offsetX[3] = 0
    offsetY[4] = 2*small.shape[0]
    offsetX[4] = small.shape[1]
    offsetY[5] = 2*small.shape[0]
    offsetX[5] = 2*small.shape[1]
    for x in range (0,6):
        background[offsetY[x]:offsetY[x]+small.shape[0], offsetX[x]:offsetX[x]+small.shape[1]] = small
    imwrite("test.jpg", background)
cv2.imshow("window", background)
cv2.waitKey()                 
cv2.destroyAllWindows()       
