import support as sup
import cv2

img = cv2.imread("van.png")

img = sup.toGray(img)
img = sup.zStretch(img, 3)

cv2.waitKey(0)
cv2.destroyAllWindows() 