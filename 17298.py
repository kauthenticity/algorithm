import sys

n = int(input());
stack = list(map(int, sys.stdin.readline().split()));
temp = list();
nge = list();

def getNGE() : 
  stack.reverse(); # make array as stack

  while stack : # while stack is not empty
    cur = stack.pop(); # get top element
    
    # break if top element is larger than current or stack is empty
    while stack and cur > stack[-1] : 
      temp.append(stack.pop());
    
    # if temp is empty 
    if not temp :
      if not stack : # that means, current element is the last one
        nge.append(-1);
       
      else : # top element is already larger than current one
        nge.append(stack[-1])

    else : 
      if not stack :
        nge.append(-1);
      else : 
        nge.append(stack[-1]);
      stack.extend(list(reversed(temp)))
      temp.clear();

getNGE();

for a in nge : 
  print(a, end=' ');