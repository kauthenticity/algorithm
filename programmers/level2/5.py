def dfs(k, visited, dungeons, cnt):
    global answer
    if False not in visited:
        if cnt > answer:
            answer = cnt
        return

    for i in range(len(visited)):
        if visited[i] == False:
            visited[i] = True
            minimum, spend = dungeons[i]

            # 해당 던전을 탐험할 수 있는 경우
            if k >= minimum:
                dfs(k - spend, visited, dungeons, cnt + 1)
            else:
                dfs(k, visited, dungeons, cnt)
            visited[i] = False


def solution(k, dungeons):
    global answer
    answer = -1

    dfs(k, [False] * len(dungeons), dungeons, 0)
    return answer


k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]
print(solution(k, dungeons))
