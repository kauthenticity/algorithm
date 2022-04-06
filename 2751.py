import sys
n = int(input())
arr = [int(sys.stdin.readline().strip()) for _ in range(n)]
arr.sort();

for a in arr : 
  print(a)