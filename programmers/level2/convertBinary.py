def convertToBinary(s):
    sLen = len(s)
    temp = ""

    while sLen > 0:
        remain = sLen % 2
        sLen = sLen // 2
        temp = str(remain) + temp

    s = temp
    return s


def removeZero(s):
    zeroNum = s.count("0")
    s = s.replace("0", "")

    s = convertToBinary(s)
    return s, zeroNum


def solution(s):
    answer = []

    zeroSum = 0
    convertCnt = 0

    while s != "1":
        s, zeroNum = removeZero(s)

        zeroSum += zeroNum
        convertCnt += 1

    answer.append(convertCnt)
    answer.append(zeroSum)

    return answer


s = "1111111"
print(solution(s))
