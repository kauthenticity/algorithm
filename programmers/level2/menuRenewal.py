from itertools import combinations


def solution(orders, course):
    answer = []

    orderNums = {}

    for menuNum in course:
        orderNums[menuNum] = {}

    for order in orders:
        order = sorted(order)
        for menuNum in course:
            combis = combinations(order, menuNum)
            for combi in combis:
                combi = "".join(combi)
                if combi not in orderNums[menuNum].keys():
                    orderNums[menuNum][combi] = 1
                else:
                    orderNums[menuNum][combi] += 1

    for menuNum in course:
        # 해당 메뉴 개수로 만들 수 있느 코스가 없으면
        if not orderNums[menuNum]:
            continue

        orderNums[menuNum] = sorted(
            orderNums[menuNum].items(), key=lambda item: item[1], reverse=True
        )

        maxOrderNum = orderNums[menuNum][0][1]
        if maxOrderNum < 2:
            continue
        maxMenu = orderNums[menuNum][0][0]
        answer.append(maxMenu)
        for i in range(1, len(orderNums[menuNum])):
            curMenu, curOrderNum = orderNums[menuNum][i]
            if curOrderNum < maxOrderNum:
                break

            answer.append(curMenu)

    answer.sort()

    return answer


orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]

print(solution(orders, course))
