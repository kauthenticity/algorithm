money = int(input())
n = int(input())
coins = list(map(int, input().split()))
coins.sort()


def getCoins(money, n, coins) : 
  dp = [(10**18)+1]*(money+1);
  print(dp)
  for coin in coins : 
    for cur in range(coin, money+1) : 
      dp[cur] = min(dp[cur-coin]+1, dp[cur])

  return dp[money]

print(getCoins(money, n, coins))

