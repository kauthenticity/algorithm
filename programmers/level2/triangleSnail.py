def solution(n):
    answer = []

    triangle = [[0 for _ in range(n)] for _ in range(n)]

    i, j = -1, 0
    m = n
    num = 1

    print(triangle)
    while m > 0:
        i += 1

        for _ in range(m):
            print("1", i, j)
            triangle[i][j] = num
            i += 1
            num += 1
        m -= 1
      
        if m == 0:
            break

        j += 1

        for _ in range(m):
            print("2", i, j)

            triangle[i][j] = num
            num += 1
            j += 1
        m -= 1

        if m == 0:
            break

        i -= 1
        j -= 1

        for _ in range(m):
            print("3", i, j)

            triangle[i][j] = num
            num += 1
            i -= 1
            j -= 1

    print(triangle)
    return answer


n = 4
print(solution(n))
