
w, h = 21, 21
Matrix = [[0 for x in range(w)] for y in range(h)] 

format = "001001110111110"

data = "0010000000100101001001111010000100100000111011000001000111101100000100011101000010010011011110001110101100010100001001000000101000101010010010011010001010001100100011101101100110100010110011110000000000111110"

Mask = [[0 for x in range(w)] for y in range(h)] 

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


