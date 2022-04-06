import sys

n = int(input());
arr = list(map(int, sys.stdin.readline().split()));

asc = [1]*n;
desc = [1]*n;
sum = [];

def increasing() : 
  for i in range(1, n) :
    for j in range(i) : 
      if arr[i] > arr[j] : 
        asc[i] = max(asc[j]+1, asc[i]);
     
def decreasing() : 
  for i in range(n-1, -1, -1) :
    for j in range(i, n) : 
      if arr[i] > arr[j] : 
        desc[i] = max(desc[j]+1, desc[i])

increasing();
decreasing();

sum = [asc[i] + desc[i] for i in range(n)]


print(max(sum)-1);