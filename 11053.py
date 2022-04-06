import sys

n = int(input());
arr = list(map(int, sys.stdin.readline().split()))
dp = [1]*n;

def longestIncreasing() : 
  for i in range(n) :
    for j in range(i) : 
      if arr[i] > arr[j] : 
        dp[i] = max(dp[j]+1, dp[i])

longestIncreasing()

print(max(dp))