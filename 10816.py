import sys

n = int(sys.stdin.readline())
As = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
Ms = list(map(int, sys.stdin.readline().split()))


def lowerBound(n, As, m):
    low = 0
    high = n - 1

    while low < high:
        mid = (low + high) // 2

        if As[mid] < m:
            low = mid + 1
        else:
            high = mid

    return high


def upperBound(n, As, m):
    low = 0
    high = n - 1

    while low < high:
        mid = (low + high) // 2

        if As[mid] <= m:
            low = mid + 1
        else:
            high = mid
    if high == n - 1 and As[high] == m:
        high += 1
    return high


def solution(n, As, m, Ms):
    answer = []

    As.sort()

    for M in Ms:
        if M < As[0] or M > As[-1]:
            answer.append(0)
        else:

            lower = lowerBound(n, As, M)
            upper = upperBound(n, As, M)

            answer.append(upper - lower)

    return answer


def printAnswer(answer):
    for ans in answer:
        print(ans, end=" ")


answer = solution(n, As, m, Ms)
printAnswer(answer)
