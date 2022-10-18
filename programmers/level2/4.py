import math


def isPrime(number):
    intNumber = int(number)

    if intNumber == 1:
        return False

    limit = int(math.sqrt(intNumber)) + 1
    for i in range(2, limit):
        if intNumber % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    digits = []
    splitted = []
    tempN = n

    while tempN > 0:
        digits.append(str(tempN % k))
        tempN //= k
    digits.reverse()

    digits = "".join(digits)
    splitted = digits.split("0")

    for num in splitted:
        if num == "":
            continue
        if isPrime(num):
            answer += 1

    return answer


n = 100049
k = 10
print(solution(n, k))
