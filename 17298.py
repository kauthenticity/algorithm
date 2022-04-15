import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().strip().split()))

def getNGE():
  stack = []
  nge = []
  loop = len(arr)

  for i in range(loop-1, -1, -1) : 
    elem = arr.pop()
    larger = -1
    
    while stack and stack[-1] <= elem : 
      stack.pop()
    
    if stack :
      larger = stack[-1]
    stack.append(elem)
    
    nge.append(larger)

  return nge
    

def printNGE(nge) : 
  for n in nge : 
    print(n, end=' ')

nge = getNGE()
nge.reverse()
printNGE(nge)