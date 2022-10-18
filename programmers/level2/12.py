def findIndices(room):
    indices = []
    for i in range(5):
        for j in range(5):
            if room[i][j] == "P":
                indices.append([i, j])
    return indices


def twoPersonOkay(p1, p2, room):
    p1x, p1y = p1
    p2x, p2y = p2

    # 맨하탄 거리가 2 이하인 경우
    if abs(p1x - p2x) + abs(p1y - p2y) <= 2:
        # 같은 column에 있는 경우
        if p1x == p2x:
            return True if room[p1x][p1y + 1] == "X" else False
        # 같은 row에 있는 경우
        elif p1y == p2y:
            return True if room[p1x + 1][p1y] == "X" else False
        # 대각선으로 있는 경우
        else:
            if p1y < p2y:
                return (
                    True
                    if room[p1x][p1y + 1] == "X" and room[p1x + 1][p1y] == "X"
                    else False
                )
            else:
                return (
                    True
                    if room[p1x][p1y - 1] == "X" and room[p1x + 1][p1y] == "X"
                    else False
                )

    else:
        return True


def isOkay(room):
    isOkay = 1

    indices = findIndices(room)

    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            # 두 명의 사람이 거리두기를 지키고 있는 지 확인
            if twoPersonOkay(indices[i], indices[j], room) == False:
                # 거리두기를 지키고 있지 않으면 0 리턴
                return 0
    return isOkay


def solution(places):
    answer = []
    for place in places:
        answer.append(isOkay(place))
    return answer


places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
]

print(solution(places))
