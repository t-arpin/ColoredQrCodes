import math
import base64

input = "TEST"

error_Correction = "10100011011111111000001110110011011011011101100000000111"

def createZero(lenght, len):
    out = ""
    max = 0
    if len == 1:
        max = 4
    elif len == 2:
        max = 7
    elif len == 8:
        max = 2*lenght
    else:
        max = len
    for i in range(max - lenght):
        out += "0"
    return out

def round_to_multiple(number, multiple):
    return multiple * math.ceil(number / multiple)

def alphaNum(data):
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

def findBestDataType(input):
    if input.isnumeric():
        return "0001"
    elif alphaNum(input) != "error":
        return "0010"
    else:
        return "0100"

def getSegment(input):
    mode = findBestDataType(input)
    sequence = []
    paddingSize = 152

    if mode == "0001":
        terminator = "0000"
        temp = ""
        data = ""
        x = 0
        for n, i in enumerate(input):
            temp += i
            x += 1
            while n == len(input) - 1:
                data += createZero(len(bin(int(temp))[2:]),len(temp)) + bin(int(temp))[2:]
                break
            while x == 3:
                data += createZero(len(bin(int(temp))[2:]),len(temp)) + bin(int(temp))[2:]
                temp = ""
                x = 0
        sequence = [mode, createZero(len(bin(len(input))[2:]),0) + bin(len(input))[2:], data, terminator]
    elif mode == "0010":
        terminator = "0000"
        temp = []
        data = ""
        x = 0
        for n, i in enumerate(input):
            temp.append(i)
            x += 1
            while n == len(input) - 1 and x != 2:
                data += createZero(len(bin(alphaNum(temp[0]))[2:]), 6) + bin(alphaNum(temp[0]))[2:]
                x = 0
                break
            while x == 2:
                data += createZero(len(bin(45*alphaNum(temp[0]) + alphaNum(temp[1]))[2:]), 11) + bin(45*alphaNum(temp[0]) + alphaNum(temp[1]))[2:]
                temp[:] = []
                x = 0  
        sequence = [mode, createZero(len(bin(len(input))[2:]), 9) + bin(len(input))[2:], data, terminator]
    else:
        return "no valid mode"

    sum = 0
    for i in sequence:
        sum += len(i)
    sequence.append(createZero((round_to_multiple(sum, 8) - sum), 8))

    sum = paddingSize - round_to_multiple(sum, 8)
    out = ""
    while sum > 7:
        out += "11101100"
        sum -= 8
        if sum < 7:
            break
        out += "00010001"
        sum -= 8
    
    sequence.append(out)

    #add error correction

    sequence.append(error_Correction)


    return sequence[0] + sequence[1] + sequence[2] + sequence[3] + sequence[4] + sequence[5] + sequence[6]

print(getSegment(input))


#qrcode printer

w, h = 21, 21

Matrix = [[0 for x in range(w)] for y in range(h)] 

format = "111001011110011" # low patern 1

data = getSegment(input)

Mask = [[0 for x in range(w)] for y in range(h)] 

def printMatix(matrix):
    out = ""
    for i in range(21):
        for x in matrix[i]:
            if x == 1:
                out += "◼ "
            else:
                out += "  "
        out += "\n"
    out += ""
    return out

def drawTimeing():
    Matrix[0][6] = 1
    Matrix[1][6] = 0
    Matrix[2][6] = 1
    Matrix[3][6] = 0
    Matrix[4][6] = 1
    Matrix[5][6] = 0
    Matrix[6][6] = 1
    Matrix[7][6] = 0
    Matrix[8][6] = 1
    Matrix[9][6] = 0
    Matrix[10][6] = 1
    Matrix[11][6] = 0
    Matrix[12][6] = 1
    Matrix[13][6] = 0
    Matrix[14][6] = 1
    Matrix[15][6] = 0
    Matrix[16][6] = 1
    Matrix[17][6] = 0
    Matrix[18][6] = 1
    Matrix[19][6] = 0
    Matrix[20][6] = 1

    Matrix[6][0] = 1
    Matrix[6][1] = 0
    Matrix[6][2] = 1
    Matrix[6][3] = 0
    Matrix[6][4] = 1
    Matrix[6][5] = 0
    Matrix[6][6] = 1
    Matrix[6][7] = 0
    Matrix[6][8] = 1
    Matrix[6][9] = 0
    Matrix[6][10] = 1
    Matrix[6][11] = 0
    Matrix[6][12] = 1
    Matrix[6][13] = 0
    Matrix[6][14] = 1
    Matrix[6][15] = 0
    Matrix[6][16] = 1
    Matrix[6][17] = 0
    Matrix[6][18] = 1
    Matrix[6][19] = 0
    Matrix[6][20] = 1

def drawFinder(x, y):
    i = 0 + x
    while i < 7 + x: 
        Matrix[i][0 + y] = 1
        i += 1
    i = 0 + x
    while i < 7 + x: 
        Matrix[i][6 + y] = 1
        i += 1
    i = 0 + y
    while i < 7 + y: 
        Matrix[0 + x][i] = 1
        i += 1
    i = 0 + y
    while i < 7 + y: 
        Matrix[6 + x][i] = 1
        i += 1

    i = 1 + x
    while i < 6 + x: 
        Matrix[i][1 + y] = 0
        i += 1
    i = 1 + x
    while i < 6 + x: 
        Matrix[i][5 + y] = 0
        i += 1
    i = 1 + y
    while i < 6 + y: 
        Matrix[1 + x][i] = 0
        i += 1
    i = 1 + y
    while i < 6 + y: 
        Matrix[5 + x][i] = 0
        i += 1

    i = 2 + x
    while i < 5 + x: 
        Matrix[i][2 + y] = 1
        i += 1
    i = 2 + x
    while i < 5 + x: 
        Matrix[i][4 + y] = 1
        i += 1
    i = 2 + y
    while i < 5 + y: 
        Matrix[2 + x][i] = 1
        i += 1
    i = 2 + y
    while i < 5 + y: 
        Matrix[4 + x][i] = 1
        i += 1
 
    Matrix[3 + x][3 + y] = 1

def drawline(x, y, len, direction, fill):
    if direction == "hori":
        for i in range(len):
            Matrix[y][x + i] = fill
    if direction == "vert":
        for i in range(len):
            Matrix[y + i][x] = fill

def drawlineMask(x, y, len, direction, fill):
    if direction == "hori":
        for i in range(len):
            Mask[y][x + i] = fill
    if direction == "vert":
        for i in range(len):
            Mask[y + i][x] = fill

def upscan(col, row, len, data, indexOff):
    di = 0
    for i in range(len):
        Matrix[row - i][col] = int(data[di + indexOff])
        di += 1
        Matrix[row - i][col - 1] = int(data[di + indexOff])
        di += 1
    return di + indexOff

def downscan(col, row, len, data, indexOff):
    di = 0
    for i in range(len):
        Matrix[row + i][col] = int(data[di + indexOff])
        di += 1
        Matrix[row + i][col - 1] = int(data[di + indexOff])
        di += 1
    return di + indexOff

def drawzigzag(data):
    downscan(1, 9, 4, data, upscan(3, 12, 4, data, downscan(5, 9, 4, data, upscan(8, 12, 4, data, downscan(10, 7, 14, data, downscan(10, 0, 6, data, upscan(12, 5, 6, data, upscan(12, 20, 14, data, downscan(14, 9, 12, data, upscan(16, 20, 12, data, downscan(18, 9, 12, data, upscan(20, 20, 12, data, 0))))))))))))

def createMask():
    drawlineMask(9, 0, 4, "hori", 1)
    drawlineMask(9, 2, 4, "hori", 1)
    drawlineMask(9, 4, 4, "hori", 1)
    drawlineMask(9, 8, 4, "hori", 1)
    drawlineMask(0, 10, 6, "hori", 1)
    drawlineMask(7, 10, 14, "hori", 1)
    drawlineMask(0, 12, 6, "hori", 1)
    drawlineMask(7, 12, 14, "hori", 1)
    drawlineMask(9, 14, 12, "hori", 1)
    drawlineMask(9, 16, 12, "hori", 1)
    drawlineMask(9, 18, 12, "hori", 1)
    drawlineMask(9, 20, 12, "hori", 1)


def drawMask(mask, matrix):
    for i in range(len(matrix)):
        for x in range(len(matrix[i])):
            matrix[i][x] = matrix[i][x] ^ mask[i][x]

def drawDataLine(x, y, len, direction, data, indexOff):
    di = 0
    if direction == "hori":
        for i in range(len):
            Matrix[y][x + i] = int(data[i + indexOff])
            di += 1
    if direction == "vert":
        for i in range(len):
            Matrix[y - i][x] = int(data[i + indexOff])
            di += 1
    return di + indexOff

def darwFormat(format):
    drawDataLine(8, 5, 6, "vert", format, drawDataLine(8, 7, 1, "vert", format, drawDataLine(7, 8, 2, "hori", format, drawDataLine(0, 8, 6, "hori", format, 0))))
    drawDataLine(13, 8, 8, "hori", format, 7)
    drawDataLine(13, 8, 8, "hori", format, 7)
    drawDataLine(8, 20, 7, "vert", format, 0)
    Matrix[13][8] = 1

drawTimeing()
drawFinder(0, 0)
drawFinder(0, 14)
drawFinder(14, 0)
drawzigzag(data)
createMask()
drawMask(Mask, Matrix)
darwFormat(format)

print("\n") 

print(printMatix(Matrix)) 

print("\n") 