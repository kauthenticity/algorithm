from collections import deque


def solution(progresses, speeds):
    answer = []

    progressStack = deque(progresses)
    speedStack = deque(speeds)

    while progressStack:
        print(progressStack, speedStack)
        while progressStack[0] < 100:
            for i in range(len(progressStack)):
                progressStack[i] += speedStack[i]
        cnt = 0

        while progressStack and progressStack[0] >= 100:
            progressStack.popleft()
            speedStack.popleft()
            cnt += 1

        if cnt > 0:
            answer.append(cnt)

    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))
