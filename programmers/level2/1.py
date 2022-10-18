from collections import deque


def solution(queue1, queue2):
    answer = -2

    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    limit = 2 * (len(q1) + len(q2))

    # 애초에 둘의 합을 같게 할 수 없는 경우
    if (sum1 + sum2) % 2 == 1:
        return -1

    cnt = 0  # 움직인 횟수
    while True:
        # 그리디하게 쭉 옮겼는데 결국에 한 쪽이 비게 되면 결국 둘은 같게 못 만듦. or 원래 위치로 되돌아 옴
        if len(q1) == 0 or len(q2) == 0 or cnt >= limit:
            cnt = -1
            break

        if sum1 == sum2:
            break
        elif sum1 > sum2:
            popped = q1.popleft()
            q2.append(popped)

            sum1 -= popped
            sum2 += popped
            cnt += 1
        elif sum1 < sum2:
            popped = q2.popleft()
            q1.append(popped)

            sum2 -= popped
            sum1 += popped
            cnt += 1

    answer = cnt
    return answer


queue1 = [1, 1]
queue2 = [1, 5]

# 10
# 8

print(solution(queue1, queue2))
