#converting you imaeg to pencil paint image
#pip install opencv-python

import cv2

image  = cv2.imread('/Python /Work_with_Images/3.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted_blur = 255 - gray_image
blur = cv2.GaussianBlur(inverted_blur, (21,21),0)
sketch = cv2.divide(gray_image,inverted_blur, scale=256.0)
cv2.imwrite('sketch_image.png', sketch)
# scv2.imshow(image,sketch)