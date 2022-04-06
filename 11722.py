import sys

n = int(input());
arr = list(map(int, sys.stdin.readline().split()))

# dp[i] : arr[i]를 포함하는 가장 긴 증가하는 부분 수열의 길이
dp = [1]*n;


def longestDecreasing() : 
  for i in range(n) :
    for j in range(i) : 
      if arr[i] < arr[j] : 
        dp[i] = max(dp[j]+1, dp[i])

longestDecreasing()

print(max(dp))