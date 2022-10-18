def solution(N, number):
    answer = 0

    dp = [0]
    end = number * N

    for i in range(1, end + 1):
        dp.append(i + 1)
        # i = (i + ... + i)/i
    dp[1] = 1 if N == 1 else 2

    i = 1
    while 10**i < end * 10:
        dp[int(str(N) * i)] = i
        i += 1

    for i in range(2, end):
        # dp[n-1] + n/n
        dp[i] = min(dp[i], dp[i - 1] + 2)

        toMinus = N
        cnt = 1
        while toMinus <= i:
            dp[i] = min(dp[i], dp[i - toMinus] + cnt)
            cnt += 1
            toMinus = int(str(N) * cnt)

    print(dp)

    answer = dp[number]
    return answer


N = 5
number = 12
print(solution(N, number))
