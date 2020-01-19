import cv2
import numpy as np
img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 75, 150)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=250)
for line in lines:
   x1, y1, x2, y2 = line[0]
   cv2.line(img, (x1, y1), (x2, y2), (0, 0, 128), 1)
cv2.imshow("linesEdges", edges)
cv2.imshow("linesDetected", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("linesEdges.jpg", img)
cv2.imwrite("linesDetected.jpg", img)

j = cv2.imread("linesEdges.jpg", 1)
k = cv2.imread("linesDetected.jpg", 1)
print(j)
print(k)