import math
import base64

input = "AHDIW$%*-$GDSJ"

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
        print("num")
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
        print("alphanum")
        terminator = "0000"
        temp = []
        data = ""
        x = 0
        for n, i in enumerate(input):
            temp.append(i)
            print("temp : ", temp)
            x += 1
            while n == len(input) - 1 and x != 2:
                data += createZero(len(bin(alphaNum(temp[0]))[2:]), 6) + bin(alphaNum(temp[0]))[2:]
                print(alphaNum(temp[0]))
                print(createZero(len(bin(alphaNum(temp[0]))[2:]), 6) + bin(alphaNum(temp[0]))[2:])
                x = 0
                break
            while x == 2:
                data += createZero(len(bin(45*alphaNum(temp[0]) + alphaNum(temp[1]))[2:]), 11) + bin(45*alphaNum(temp[0]) + alphaNum(temp[1]))[2:]
                print(45*alphaNum(temp[0]) + alphaNum(temp[1]))
                print(createZero(len(bin(45*alphaNum(temp[0]) + alphaNum(temp[1]))[2:]), 11) + bin(45*alphaNum(temp[0]) + alphaNum(temp[1]))[2:])
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

    sequence.append("00000000000000000000000000000000000000000000000000000000")

    print(sequence)

    return sequence[0] + sequence[1] + sequence[2] + sequence[3] + sequence[4] + sequence[5] + sequence[6]

print(getSegment(input))

