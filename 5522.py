As = map(int, list(input() for _ in range(5)))

def sum(As) : 
  tot = 0;
  for a in As : 
    tot += a;

  return tot;

print(sum(As));