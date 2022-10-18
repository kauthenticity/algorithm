def move(matrix, query):
    x1, y1, x2, y2 = query

    x1 = x1 - 1
    y1 = y1 - 1
    x2 = x2 - 1
    y2 = y2 - 1

    minNum = matrix[x1][y1]
    next = minNum

    # 왼쪽 위
    temp = next
    next = matrix[x1][y1 + 1]
    minNum = min(minNum, next)
    matrix[x1][y1 + 1] = temp

    # 상
    for col in range(y1 + 1, y2):
        temp = next
        next = matrix[x1][col + 1]
        minNum = min(minNum, next)

        matrix[x1][col + 1] = temp
    # 오른쪽 위
    temp = next
    next = matrix[x1 + 1][y2]
    minNum = min(minNum, next)

    matrix[x1 + 1][y2] = temp

    # 우
    for row in range(x1 + 1, x2):
        temp = next
        next = matrix[row + 1][y2]
        minNum = min(minNum, next)
        matrix[row + 1][y2] = temp

    # 오른쪽 아래
    temp = next
    next = matrix[x2][y2 - 1]
    minNum = min(minNum, next)

    matrix[x2][y2 - 1] = temp

    # 하
    for col in range(y2, y1, -1):
        temp = next
        next = matrix[x2][col - 1]
        minNum = min(minNum, next)

        matrix[x2][col - 1] = temp

    # 왼쪽 아래
    temp = next
    next = matrix[x2 - 1][y1]
    minNum = min(minNum, next)
    matrix[x2 - 1][y1] = temp

    # 좌
    for row in range(x2 - 1, x1, -1):
        temp = next
        next = matrix[row - 1][y1]
        minNum = min(minNum, next)
        matrix[row - 1][y1] = temp

    matrix[x1][y1] = next

    return minNum


def solution(rows, columns, queries):
    answer = []

    matrix = []

    for i in range(rows):
        matrix.append([])
        for j in range(columns):
            matrix[i].append(i * columns + j + 1)

    for query in queries:
        answer.append(move(matrix, query))
        for i in range(rows):
            for j in range(columns):
                print(matrix[i][j], end="")
            print("")
    return answer


rows = 3
columns = 3
queries = [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]

print(solution(rows, columns, queries))
