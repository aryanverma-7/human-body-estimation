import cv2
print(cv2.__version__)
img = cv2.imread('/Users/varshithaballa/Pictures/example.jpg',0)
print(img)
cv2.imshow('color_image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
status = cv2.imwrite('/Users/varshithaballa/Pictures/example.jpg',img)
print("Image written to file System:", status)
