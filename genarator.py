import math
import base64

str = "ABC"

def findBestDataType(str):
    if str.isnumeric():
        return "0001"
    elif str.isalnum() and str.isupper():
        return "0010"
    else:
        return "0100"

def createZero(lenght, len):
    out = ""
    max = 0
    if len == 1:
        max = 4
    elif len == 2:
        max = 7
    elif len == 8:
        max = 2*lenght
    elif len == 11:
        max = 11
    else:
        max = 10
    for i in range(max - lenght):
        out += "0"
    return out

def round_to_multiple(number, multiple):
    return multiple * math.ceil(number / multiple)

def getSegment(str):
    mode = findBestDataType(str)
    sequence = []

    if mode == "0001":
        terminator = "0000"
        temp = ""
        data = ""
        x = 0
        for n, i in enumerate(str):
            temp += i
            x += 1
            while n == len(str) - 1:
                data += createZero(len(bin(int(temp))[2:]),len(temp)) + bin(int(temp))[2:]
                break
            while x == 3:
                data += createZero(len(bin(int(temp))[2:]),len(temp)) + bin(int(temp))[2:]
                temp = ""
                x = 0
        sequence = [mode, createZero(len(bin(len(str))[2:]),0) + bin(len(str))[2:], data, terminator]
    elif mode == "0010":
        terminator = "0000"
        temp = []
        data = ""
        x = 0
        for n, i in enumerate(str):
            temp.append(i)
            x += 1
            while n == len(str) - 1:
                data += bin(ord(temp[0]))[2:]
                break
            while x == 2:
                data += createZero(len(bin(45*ord(temp[0]) + ord(temp[1]))[2:]), 11) + bin(45*ord(temp[0]) + ord(temp[1]))[2:]
                temp.clear
                x = 0
                print(len(temp))
        sequence = [mode, createZero(len(bin(len(str))[2:]),0) + bin(len(str))[2:], data, terminator]

    sum = 0
    for i in sequence:
        sum += len(i)
    sequence.append(createZero((round_to_multiple(sum, 8) - sum), 8))

    sum = 152 - round_to_multiple(sum, 8)
    out = ""
    while sum > 7:
        out += "11101100"
        sum -= 8
        if sum < 7:
            break
        out += "00010001"
        sum -= 8
    
    sequence.append(out)

    print(sequence)

    return sequence[0] + sequence[1] + sequence[2] + sequence[3] + sequence[4] + sequence[5]

print(getSegment(str))

