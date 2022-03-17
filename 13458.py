def calcSupervisor(n, students, b, c) : 
  sum = n
  for student in students :
    rests = student-b;

    if rests > 0 and rests < c : 
      sum += 1;
    else : 
      sum += ((student-b-1)//c)+1;
    
  print(sum);


n = int(input())
students = list(map(int, input().split()))
b, c = map(int, input().split())

calcSupervisor(n, students, b, c)