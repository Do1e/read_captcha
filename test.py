import cv2
import numpy as np

s = np.zeros([100, 100, 3], np.uint8)
cv2.imshow("test", s)
key = cv2.waitKey(0)
print(key)
cv2.destroyAllWindows()