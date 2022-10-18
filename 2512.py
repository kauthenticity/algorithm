import sys

n = int(sys.stdin.readline())
budgets = list(map(int, sys.stdin.readline().split()))
amt = int(sys.stdin.readline())


def solution(n, budgets, amt):
    answer = 0
    budgets.sort()
    low = 1
    high = budgets[-1]

    while low <= high:
        mid = (low + high) // 2

        curAmt = 0
        for budget in budgets:
            if budget <= mid:
                curAmt += budget
            else:
                curAmt += mid

        if curAmt <= amt:
            low = mid + 1
        else:
            high = mid - 1

    answer = high
    return answer


print(solution(n, budgets, amt))
