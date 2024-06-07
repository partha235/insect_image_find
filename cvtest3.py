import cv2
import numpy as np

threshold_value = 100 
img_p="insect1.jpg"
img=cv2.imread(img_p,cv2.IMREAD_GRAYSCALE)

# Naming a window 
# cv2.namedWindow("image", cv2.WINDOW_NORMAL) 
# cv2.resizeWindow("insect",500,500)

_, binary_image = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)

inverted_binary_image = cv2.bitwise_not(binary_image)
contours, _ = cv2.findContours(inverted_binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
original_image = cv2.imread(img_p)
cv2.drawContours(original_image, contours, -1, (0, 255, 0), 2)
dark_object_count = len(contours)
print(len(contours))

cv2.imshow('image', original_image)
cv2.waitKey()
cv2.destroyAllWindows()