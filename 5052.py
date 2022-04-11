import sys
import functools

t = int(input())

def cmp(a, b) :
  n = min(len(a), len(b))

  for i in range(n) : 
    if a[i] < b[i] : 
      return -1
    elif a[i] > b[i] : 
      return 1

  if len(a) < len(b) : 
    return -1
  elif len(a) > len(b) : 
    return 1
  else : 
    return 0

def consistency(n, phones) : 
  phones = sorted(phones, key=functools.cmp_to_key(cmp))
  
  for i in range(1, len(phones)) : 
    preLen = len(phones[i-1])
    if phones[i-1]  == phones[i][0:preLen] : 
      return 'NO'
  
  return 'YES'


def getInput() : 
  for _ in range(t) : 
    n = int(input())
    phones = [sys.stdin.readline().strip() for _ in range(n)]
    ans = consistency(n, phones)

    print(ans)


getInput()