conditionTree = {
    "java": {
        "backend": {
            "junior": {"chicken": [], "pizza": []},
            "senior": {"chicken": [], "pizza": []},
        },
        "frontend": {
            "junior": {"chicken": [], "pizza": []},
            "senior": {"chicken": [], "pizza": []},
        },
    },
    "cpp": {
        "backend": {
            "junior": {"chicken": [], "pizza": []},
            "senior": {"chicken": [], "pizza": []},
        },
        "frontend": {
            "junior": {"chicken": [], "pizza": []},
            "senior": {"chicken": [], "pizza": []},
        },
    },
    "python": {
        "backend": {
            "junior": {"chicken": [], "pizza": []},
            "senior": {"chicken": [], "pizza": []},
        },
        "frontend": {
            "junior": {"chicken": [], "pizza": []},
            "senior": {"chicken": [], "pizza": []},
        },
    },
}


def fillConditionTree(info):
    global conditionTree
    for condition in info:
        a, b, c, d, e = condition.split(" ")
        conditionTree[a][b][c][d].append(int(e))


def count(q):
    res = 0
    words = q.split(" ")
    condition = [words[0], words[2], words[4], words[6], int(words[7])]

    match = []
    conditionList = []
    for i in range(4):
        if condition[i] == "-":
            if i == 0:
                conditionList.append(["cpp", "java", "python"])
            elif i == 1:
                conditionList.append(["backend", "frontend"])
            elif i == 2:
                conditionList.append(["senior", "junior"])
            elif i == 3:
                conditionList.append(["chicken", "pizza"])
        else:
            conditionList.append([condition[i]])

    for a in conditionList[0]:
        for b in conditionList[1]:
            for c in conditionList[2]:
                for d in conditionList[3]:
                    match.extend(conditionTree[a][b][c][d])
    for score in match:
        if score >= condition[4]:
            res += 1
    return res


def solution(info, query):
    answer = []

    fillConditionTree(info)

    for q in query:
        answer.append(count(q))

    return answer


info = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50",
]
query = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150",
]

print(solution(info, query))
