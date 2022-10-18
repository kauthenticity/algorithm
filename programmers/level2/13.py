def convertToBit(n):
    bitString = ""

    if n == 0:
        return "0"

    while n > 0:
        bitString = str(n % 2) + bitString
        n = n // 2
    # bitString = str(n) + bitString

    return bitString


def bitToNumber(bit):
    bitLen = len(bit)
    res = 0
    for i in range(bitLen):
        if bit[i] == "1":
            res += 2 ** (bitLen - i - 1)

    return res


def getNumber(n):
    res = 1
    bit = convertToBit(n)

    print(bit)
    # 맨 끝자리가 0인 경우
    if bit[-1] == "0":
        res = n + 1
    elif "0" in bit:
        for i in range(len(bit) - 1, -1, -1):
            if bit[i] == "0":
                break
        temp = bit[:i] + "10" + bit[i + 2 :]
        res = bitToNumber(temp)
    else:
        res = n + 2 ** (len(bit) - 1)
    return res


def solution(numbers):
    answer = []

    for number in numbers:
        answer.append(getNumber(number))

    return answer


numbers = [15]
print(solution(numbers))

"""
1. 0이 있는 경우

1-1. 0이 제일 끝자리인 경우
1110 -> 1111
0을 1로 바꾸기

1-2. 0이 제일 끝자리가 아닌 경우
제일 아랫자리 0을 찾아서 1로 바꾸고, 그 아랫자리수를 0으로 바꾸기
110101 : 1 + 4 + 16 + 32 = 53
110110 :54

2. 0이 없는 경우 (맨 앞에 0이 붙어있다 가정)
01111 : (15)
일단 맨 앞에 1 추가 (이미 차이 1)
11111
-> [1]을 0으로 바꾸기
11111 -> 10111 : 16 + 7 = 23

011111 : 31 (1 + 2 + 4 + 8 + 16)
101111  : 47 (1 + 2 + 4 + 8 + 32)

101111
110111


1111
"""
