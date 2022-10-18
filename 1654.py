import sys

# k, n = map(int, (sys.stdin.readline().split()))
# lans = []

# for i in range(k):
#     lans.append(int(sys.stdin.readline()))


def solution(k, n, lans):
    answer = 0

    lans.sort()

    low = 1
    high = lans[-1]

    while low <= high:
        mid = (low + high) // 2

        cnt = 0
        for lan in lans:
            cnt += lan // mid
        if cnt >= n:
            low = mid + 1
        else:
            high = mid - 1
    answer = high
    return answer


# print(solution(k, n, lans))

print(solution(4, 11, [802, 743, 457, 539]))
print(solution(4, 4, [200, 200, 200, 200]))
print(solution(2, 4, [100, 1]))
print(solution(4, 8, [13, 13, 13, 13]))
print(solution(4, 1, [802, 743, 457, 539]))
print(solution(4, 4, [200, 200, 200, 1]))
print(solution(4, 15, [802, 743, 457, 539]))
print(solution(5, 6, [1, 1, 1, 1, 11]))
print(solution(2, 2, [5, 10]))
print(solution(2, 2, [1, 2147483647]))
