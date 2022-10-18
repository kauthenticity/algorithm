from collections import deque


def makeGraph(wires):
    graph = {}

    for wire in wires:
        v1, v2 = wire

        if v1 not in graph.keys():
            graph[v1] = []
        if v2 not in graph.keys():
            graph[v2] = []

        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph


def bfs(graph, n):
    queue = deque()
    visited = [False] * n

    """
    graph = {
        1 : [3],
        2 : [3],
        3 : [1, 2, 4],
        4 : [3, 5, 6],
        5 : [4],
        6 : [4],
        7 : [8, 9],
        8 : [7],
        9 : [7]
    }
    """
    # Visited가 True인 것과 False인 것의 차의 절댓값을 구하면 됨.

    first = list(graph.keys())[0]
    queue.append(first)
    visited[first - 1] == True

    while queue:
        v = queue.popleft()
        for vertex in graph[v]:
            if visited[vertex - 1] == False:
                visited[vertex - 1] = True
                queue.append(vertex)

    return abs(visited.count(True) - visited.count(False))


def getDiff(wires, n):
    graph = makeGraph(wires)
    return bfs(graph, n)


def solution(n, wires):
    answer = 1001

    for i in range(len(wires)):
        # wire하나 씩 제거
        tempWires = wires[:i] + wires[i + 1 :]
        answer = min(answer, getDiff(tempWires, n))

    return answer


n = 9
wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]
print(solution(n, wires))
