from itertools import permutations


def calc(perm, expression, idx):
    res = 0

    if idx > 2:
        return int(expression)
    tokens = expression.split(perm[idx])

    for i in range(len(tokens)):
        if i == 0:
            res = calc(perm, tokens[i], idx + 1)
        else:
            if perm[idx] == "+":
                res += calc(perm, tokens[i], idx + 1)
            elif perm[idx] == "*":
                res *= calc(perm, tokens[i], idx + 1)
            elif perm[idx] == "-":
                res -= calc(perm, tokens[i], idx + 1)

    return abs(res)


def solution(expression):
    answer = 0
    operations = ["+", "-", "*"]
    perms = permutations(operations, 3)

    for perm in perms:
        answer = max(answer, calc(perm, expression, 0))

    return answer


expression = "50*6-3*2"
print(solution(expression))
