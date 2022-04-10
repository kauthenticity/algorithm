import sys

str = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

def explode() : 
  stack = []
  bombLen = len(bomb) # bomb length
  
  for i in range(len(str)) : 
    stack.append(str[i])
    
    # stack의 top이 폭발 문자열의 끝과 같을 경우 뒤에서 앞으로 탐색하며 문자열 비교
    if stack[-1] == bomb[bombLen-1] : 
      stackLen = len(stack)
      inStack = ''.join(stack[stackLen-bombLen : stackLen])

      if inStack == bomb : 
        for i in range(bombLen) :
          stack.pop()

  stack = 'FRULA' if not stack else ''.join(stack)
  return stack

ans = explode()
print(ans)