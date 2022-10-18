def getArr(i, j, n, isLeft):
    tempArr = [i + 1] * (i + 1)

    for it in range(i + 2, n + 1):
        tempArr.append(it)
    return tempArr[j:] if isLeft == True else tempArr[0 : j + 1]


def solution(n, left, right):
    answer = []

    i1 = (left) // n
    j1 = (left) % n
    i2 = (right) // n
    j2 = (right) % n

    start = i1
    j = j1

    if i1 == i2:
        tempArr = [i1 + 1] * (i1 + 1)

        for it in range(i1 + 2, n + 1):
            tempArr.append(it)
        answer = tempArr[j1 : j2 + 1]

    else:
        while start < i2:
            answer += getArr(start, j, n, True)
            j = 0
            start += 1
        answer += getArr(i2, j2, n, False)

    return answer


n = 4
left = 7
right = 8

print(solution(n, left, right))
