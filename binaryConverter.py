# Python: Binary to Decimal Conversion

def convert(fromNum, fromBase, toBase):

    toNum = 0
    power = 0
    while fromNum > 0:
        toNum += fromBase ** power * (fromNum % toBase)
        fromNum //= toBase
        power += 1

#    return toNum
    print(str(toNum))

convert(12, 10, 8)

convert(1000001, 2, 10)


# Python Hexadecimal to Decimal Conversion

def __getDecDigit(digit):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    for x in range (len(digits)):
        if digit == digits[x]:
            return x

def hexToDec(hexNum):
    decNum = 0
    power = 0
    for digit in range(len(hexNum) , 0, -1):
        decNum = decNum + 16 ** power * __getDecDigit(hexNum[digit-1])
        power += 1

    print(str(decNum))

hexToDec('20')
