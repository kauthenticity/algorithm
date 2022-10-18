import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


def replaceLis(num, lis):
    low = 0
    high = len(lis)

    while low < high:
        mid = (low + high) // 2

        if lis[mid] < num:
            low = mid + 1
        else:
            high = mid

    if lis[high] != num:
        lis[high] = num

    return


def solution(n, arr):
    answer = 0
    lis = []  # lis[i] : 길이가 i+1인 arr에서 제일 큰 수
    lis.append(arr[0])

    for i in range(1, n):

        # 내가 더 크면
        if arr[i] > lis[-1]:
            lis.append(arr[i])
        elif arr[i] == lis[-1]:
            continue
        else:
            replaceLis(arr[i], lis)
    answer = len(lis)
    return answer


print(solution(n, arr))
