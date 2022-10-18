def calc(expression, perm):
    for operator in perm:
        temp = expression.split(operator)
        print(temp)


def solution(expression):
    answer = 0
    # +, -, * 의 우선순위. 숫자가 낮을수록 높은 우선순위.
    perms = [
        ["+", "-", "*"],
        ["+", "*", "-"],
        ["*", "-", "+"],
        ["*", "+", "-"],
        ["-", "+", "*"],
        ["-", "*", "+"],
    ]

    for perm in perms:
        res = calc(expression, perm)
        # answer = max(answer, res)

    return answer


expression = "100-200*300-500+20"
print(solution(expression))
