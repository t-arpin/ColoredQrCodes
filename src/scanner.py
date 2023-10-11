import cv2
import numpy as np
from pyzbar.pyzbar import decode

dectedqr = False
qrtries = 0
Matrix = [[0 for x in range(21)] for y in range(21)]
windowsSize = [21, 21]
scaling = 18
sens = 30

def decoder(image):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
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
    if dectedqr == True and qrtries == sens:
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
    cv2.imshow("Image", frame)
    code = cv2.waitKey(10)
    if code == ord('q'):
        break

#whitepoint
temp = img_output[1*10:1*10+10, 1*10:1*10+10]
average = temp.mean(axis=0).mean(axis=0)
whitepoint = (average[0] + average[1] + average[2])/3
#blackpoint
temp = img_output[0*10:0*10+10, 0*10:0*10+10]
average = temp.mean(axis=0).mean(axis=0)
print(average)
blackpoint = (average[0] + average[1] + average[2])/3
#bluepoint
temp = img_output[2*10:2*10+10, 2*10:2*10+10]
average = temp.mean(axis=0).mean(axis=0)
bluepoint = average[0]
#redpoint
temp = img_output[2*10:2*10+10, 18*10:18*10+10]
average = temp.mean(axis=0).mean(axis=0)
redpoint = average[1]
#greenpoint
temp = img_output[18*10:18*10+10, 2*10:2*10+10]
average = temp.mean(axis=0).mean(axis=0)
greenpoint = average[2]

cv2.imshow("Image", img_output)
cv2.waitKey(10)


print("whitepoint : ", whitepoint)
print("blackpoint : ", blackpoint)
print("redpoint : ", redpoint)
print("greenpoint : ", greenpoint)
print("bluepoint : ", bluepoint)

def between(x, point, dev):
  return x >= point - dev and x <= point + dev

dev = 30
cdev = 1

for y in range(21):
  for x in range(21):
    temp = img_output[y*10:y*10+10, x*10:x*10+10]
    average = temp.mean(axis=0).mean(axis=0)
    #white
    if between((average[0] + average[1] + average[2])/3,  whitepoint, dev):
        Matrix[y][x] = 0
    #black
    elif between((average[0] + average[1] + average[2])/3,  blackpoint, dev):
        Matrix[y][x] = 1
    #blue
    elif between(average[0], bluepoint, cdev) and between((average[1] + average[2])/2, blackpoint, dev):
        Matrix[y][x] = 2
    #red
    elif between(average[1], redpoint, cdev) and between((average[0] + average[2])/2, blackpoint, dev):
        Matrix[y][x] = 3
    #green
    elif between(average[2], greenpoint, cdev) and between((average[1] + average[0])/2, blackpoint, dev):
        Matrix[y][x] = 4
  

img = np.zeros((windowsSize[0]*scaling, windowsSize[1]*scaling, 3), np.uint8)

for y in range(21):
    for x, i in enumerate(Matrix[y]):
        if i == 0:
            img[y*scaling:y*scaling+scaling, x*scaling:x*scaling+scaling] = (255, 255, 255)
        elif i == 1:
            img[y*scaling:y*scaling+scaling, x*scaling:x*scaling+scaling] = (0, 0, 0)
        elif i == 2:
            img[y*scaling:y*scaling+scaling, x*scaling:x*scaling+scaling] = (255, 0, 0)
        elif i == 3:
            img[y*scaling:y*scaling+scaling, x*scaling:x*scaling+scaling] = (0, 255, 0)
        elif i == 4:
            img[y*scaling:y*scaling+scaling, x*scaling:x*scaling+scaling] = (0, 0, 255)

cv2.imshow("image", img)
cv2.waitKey(0)
