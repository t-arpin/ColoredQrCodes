def alpha_to_num(data):
  charstr ="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:"
  out = ""
  chars = list(charstr)
  nums = [str(i) for i in range(0,44)]
  alphanumTable = dict(zip(chars,nums))
  for i in data:
    if i in charstr:
      out += alphanumTable[i]
    else:
      return "error"
  return(int(out))
  

print(alpha_to_num("Te"))

import cv2
import numpy as np

img = cv2.imread("QRCODE.png")

Matrix = [[0 for x in range(21)] for y in range(21)] 

for y in range(21):
  for x in range(21):
    temp = img[y*10:y*10+10, x*10:x*10+10]
    average = temp.mean(axis=0).mean(axis=0)
    if (average[0] + average[1] + average[2])/3 >= 200:
      Matrix[y][x] = 0
    else:
      Matrix[y][x] = 1

def printMatix(matrix):
    out = ""
    for i in range(21):
        for x in matrix[i]:
            if x == 1:
                out += "██"
            else:
                out += "  "
        out += "\n"
    out += ""
    return out

print(printMatix(Matrix))