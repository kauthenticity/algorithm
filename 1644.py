n = int(input())
a = [False, False] + [True] * (n-1)
primes = []


def getPrimes(n):
    for i in range(2, n+1):
        if a[i]:
            primes.append(i)
            for j in range(i+i, n+1, i):
                a[j] = False


def getWays(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    res = 0
    sum = 0
    low = 0
    high = 0

    while(high < len(primes) and low < len(primes)):
        if sum < n:
            sum += primes[high]
            high += 1
        elif sum >= n:
            sum -= primes[low]
            low += 1

        if sum == n:
            res += 1

    if n == primes[high - 1]:
        res += 1

    return res


getPrimes(n)

print(getWays(n))
