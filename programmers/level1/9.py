def solution(n, lost, reserve):
    answer = 0

    lost.sort()
    reserve.sort()
    saved = 0  # 체육복을 구한 사람 수

    i = 0
    all = len(lost)

    while i < all:
        losted = lost[i]
        if losted in reserve:
            lost.remove(losted)
            reserve.remove(losted)
            all = len(lost)
        else:
            i += 1

    for num in lost:
        if num - 1 in reserve:
            reserve.remove(num - 1)
            saved += 1
        elif num + 1 in reserve:
            reserve.remove(num + 1)
            saved += 1
    answer = n - (len(lost) - saved)

    return answer


n = 5
lost = [2, 3, 5]
reserve = [2, 3, 5]
# lost = [2, 4, 5]
# reserve = [1, 3, 4]

print(solution(n, lost, reserve))


# ex : n=10, lost = [3, 5, 7], reserve = [4, 6, 9]
