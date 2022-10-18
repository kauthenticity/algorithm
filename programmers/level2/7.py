from operator import itemgetter


def getCrossedPoint(line1, line2):
    a, b, e = line1
    c, d, f = line2

    # 평행하는 경우 교점이 없음
    if a * d - b * c == 0:
        return []

    shared = a * d - b * c
    x = (b * f - e * d) / shared
    y = (e * c - a * f) / shared

    return [x, y]


def trimSolution(points, answer):
    ys = []
    xs = []

    res = []

    for point in points:
        x, y = point
        ys.append(y)
        xs.append(x)

    maxY = max(ys)
    minY = min(ys)

    minX = min(xs)
    maxX = max(xs)

    col = maxX - minX + 1
    row = maxY - minY + 1

    for i in range(row):
        res.append([])
        for _ in range(col):
            res[i].append(".")
    for point in points:
        x, y = point
        offsetX = x - minX
        offsetY = maxY - y

        res[offsetY][offsetX] = "*"

    for line in res:
        tempLine = "".join(line)
        answer.append(tempLine)


def solution(line):
    answer = []
    crossed = []

    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            crossedPoint = getCrossedPoint(line[i], line[j])
            if not crossedPoint:
                continue

            x, y = crossedPoint

            if int(x) == x and int(y) == y:
                crossed.append([int(x), int(y)])

    trimSolution(crossed, answer)

    return answer


line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
print(solution(line))
