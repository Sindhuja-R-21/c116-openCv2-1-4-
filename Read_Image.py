import cv2

#Read image
img=cv2.imread("C:/Users/HP/Desktop/Python WH class/c116/butterfly.jpg")

#Display colored image
cv2.imshow("Colorful_butterfly",img)

#Convert colored image into grayscale
gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

cv2.imshow("GrayScale_Image",gray_img)


cv2.waitKey(0)