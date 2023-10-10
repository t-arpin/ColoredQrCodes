import cv2
import numpy as np
from pyzbar.pyzbar import decode

dectedqr = False

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
    if dectedqr == True:
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

        cv2.imwrite("QRCODE.png", img_output)
        break
    else:
        cv2.imshow("Image", frame)
        code = cv2.waitKey(10)
    if code == ord('q'):
        break
