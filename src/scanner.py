import cv2
import numpy as np
from pyzbar.pyzbar import decode

dectedqr = False
qrtries = 0
Matrix = [[0 for x in range(21)] for y in range(21)]
windowsSize = [21, 21]
scaling = 18

def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    qrcode = decode(gray_img)

    for obj in qrcode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        #cv2.polylines(image, [pts], True, (0, 255, 0), 3)
        return True, points
    return False, []
        

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    dectedqr, point = decoder(frame)
    if dectedqr == True and qrtries == 20:
        p1 = [point[0][0], point[0][1]]
        p3 = [point[1][0], point[1][1]]
        p4 = [point[2][0], point[2][1]]
        p2 = [point[3][0], point[3][1]]

        width = 210
        height = 210

        input_points = np.float32([p1, p2, p3, p4])
        converted_points = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(input_points, converted_points)
        img_output = cv2.warpPerspective(frame, matrix, (width, height))
        cv2.destroyAllWindows()       
        break
    if dectedqr == True:
        qrtries += 1
    else:
        cv2.imshow("Image", frame)
        code = cv2.waitKey(10)
    if code == ord('q'):
        break

for y in range(21):
  for x in range(21):
    temp = img_output[y*10:y*10+10, x*10:x*10+10]
    average = temp.mean(axis=0).mean(axis=0)
    if (average[0] + average[1] + average[2])/3 >= 200:
      Matrix[y][x] = 0
    else:
      Matrix[y][x] = 1


img = np.zeros((windowsSize[0]*scaling, windowsSize[1]*scaling, 3), np.uint8)

for y in range(21):
  for x, i in enumerate(Matrix[y]):
      if i == 1:
          img[y*scaling:y*scaling+scaling, x*scaling:x*scaling+scaling] = (0, 0, 0)
      else:
          img[y*scaling:y*scaling+scaling, x*scaling:x*scaling+scaling] = (255, 255, 255)

cv2.imshow("image", img)
cv2.waitKey(0)
