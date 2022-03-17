def calcSupervisor(n, students, b, c) : 
  sum = n
  for student in students :
    rests = student-b;

    if rests == 0 or rests < 0 :
      continue;
    else : 
      sum += ((rests-1)//c)+1;
    
  return sum


n = int(input())
students = list(map(int, input().split()))
b, c = map(int, input().split())

sum = calcSupervisor(n, students, b, c)
print(sum)