w, h = map(int, input().split());
p, q = map(int, input().split());
t = int(input());

def getDir(x, y, dir):
  if x == 0:
    if y == 0:
      dir = (1, 1);
    else:
      if dir == (-1, -1):
        dir = (1, -1);
      else:
        dir = (1, 1);
  elif x == w : 
    if y == h :
      dir = (-1, -1);
    else : 
      if dir == (1, 1) : 
        dir = (-1, 1);
      else : 
        dir = (-1, -1);
  elif y == 0 :
    if dir == (-1, -1):
      dir = (-1, 1)
    else:
      dir = (1, 1)
  elif y == h :
    if dir == (1, 1) : 
      dir = (1, -1);
    else : 
      dir = (-1, -1);

def getPosition(w, h, p, q, t) : 
  i = 0;
  x = p;
  y = q;

  dir = (1, 1);
  while(i < t) : 
    
  


    

    i += 1;

  return x, y;


res = getPosition(w, h, p, q, t)
print(res[0], res[1]);