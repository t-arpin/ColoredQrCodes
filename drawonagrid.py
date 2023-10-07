
w, h = 21, 21
Matrix = [[0 for x in range(w)] for y in range(h)] 

data = "0010000000100101001001111010000100100000111011000001000111101100000100011110110000010001111011000001000111101100000100011110110000010001111011000001000110100011011111111000001110110011011011011101100000000111"


def printMatix(matrix):
    out = ""
    for i in range(21):
        for x in matrix[i]:
            if x == 1:
                out += "◽"
            else:
                out += "◾"
        out += "\n"
    return out

def drawTimeing():
    Matrix[0][5] = 1
    Matrix[1][5] = 0
    Matrix[2][5] = 1
    Matrix[3][5] = 0
    Matrix[4][5] = 1
    Matrix[5][5] = 0
    Matrix[6][5] = 1
    Matrix[7][5] = 0
    Matrix[8][5] = 1
    Matrix[9][5] = 0
    Matrix[10][5] = 1
    Matrix[11][5] = 0
    Matrix[12][5] = 1
    Matrix[13][5] = 0
    Matrix[14][5] = 1
    Matrix[15][5] = 0
    Matrix[16][5] = 1
    Matrix[17][5] = 0
    Matrix[18][5] = 1
    Matrix[19][5] = 0
    Matrix[20][5] = 1

    Matrix[5][0] = 1
    Matrix[5][1] = 0
    Matrix[5][2] = 1
    Matrix[5][3] = 0
    Matrix[5][4] = 1
    Matrix[5][5] = 0
    Matrix[5][6] = 1
    Matrix[5][7] = 0
    Matrix[5][8] = 1
    Matrix[5][9] = 0
    Matrix[5][10] = 1
    Matrix[5][11] = 0
    Matrix[5][12] = 1
    Matrix[5][13] = 0
    Matrix[5][14] = 1
    Matrix[5][15] = 0
    Matrix[5][16] = 1
    Matrix[5][17] = 0
    Matrix[5][18] = 1
    Matrix[5][19] = 0
    Matrix[5][20] = 1

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

def upscan(col, row, len, data):
    di = 0
    for i in range(len):
        Matrix[col][row - i] = data[di]
        di += 1
        Matrix[col-1][row - i] = data[di]
        di += 1

dlist = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0] 

drawTimeing()
drawFinder(0, 0)
drawFinder(0, 14)
drawFinder(14, 0)
upscan(20, 20, 5, dlist)

print("\n") 

print(printMatix(Matrix)) 

print("\n") 

