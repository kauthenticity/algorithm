import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

sum = arr[:]; # deep copy

def largestIncreasing() : 
  for i in range(n) : 
    for j in range(i) :
      if arr[j] < arr[i] : 
        sum[i] = max(sum[i], sum[j] + arr[i])

largestIncreasing()
print(max(sum))