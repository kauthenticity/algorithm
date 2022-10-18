def isBest(ryan):
    global answer

    for i in range(10, -1, -1):
        # 적은 점수를 라이언이 더 많이 맞추었다면 이게 최선
        if ryan[i] > answer[i]:
            return True
        elif ryan[i] < answer[i]:
            return False


def calcScore(appeach, ryan):
    global maxDiff, answer
    curDiff = 0  # 현재 점수 차이
    appeachScore = 0
    ryanScore = 0

    for i in range(11):
        if appeach[i] < ryan[i]:
            ryanScore += 10 - i
        elif appeach[i] > ryan[i]:
            appeachScore += 10 - i
    curDiff = ryanScore - appeachScore
    if curDiff >= maxDiff and curDiff > 0:
        if curDiff == maxDiff and isBest(ryan) == False:
            return
        answer = ryan[0:]
        maxDiff = curDiff


# 완전탐색. 10-idx점을 얻거나 안 얻거나
def dfs(idx, leftShoots, ryan, appeach):
    # 더 이상 쏠 수 있는 화살이 없는 경우 점수 계산 및 리턴
    if leftShoots == 0:
        calcScore(appeach, ryan)
        return

    # 0점에 도달한 경우 점수 계산 및 리턴
    if idx == 10:

        # 0점에 도달했는데 화살이 남은 경우
        if leftShoots > 0:
            ryan[10] = leftShoots
        calcScore(appeach, ryan)
        ryan[10] = 0
        return

    # 10-idx 점 얻기
    if leftShoots > appeach[idx]:
        # 어피치보다 한 발 더 맞춤
        ryanShoot = appeach[idx] + 1
        ryan[idx] = ryanShoot
        dfs(idx + 1, leftShoots - ryanShoot, ryan, appeach)

    # 10 - idx 점 안 얻기
    ryan[idx] = 0
    dfs(idx + 1, leftShoots, ryan, appeach)


def solution(n, info):
    global answer, maxDiff

    maxDiff = -1
    answer = [-1]

    dfs(0, n, [0] * 11, info)

    return answer


n = 1
info = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(solution(n, info))
