n = int(input());
upper = 10000000;
bound = int(upper**(0.5))
visited = [False, False] + [True] * (upper-1);
primes = [];

def getPrimes() : 
  for i in range(2, bound+1) : 
    if visited[i] : 
      for j in range(i+i, upper+1, i) : 
        visited[j] = False;

  for i in range(2, upper+1) : 
    if visited[i] : 
      primes.append(i);

def findStart(n) :
  pre = -1;
  for i in range(len(primes)) :
    if pre < n and n <= primes[i] : 
      return i;
    pre = primes[i];

def isPalindrome(num) : 
  temp = str(num);
  half = len(temp)//2;
  for i in range(half) : 
    if temp[i] != temp[len(temp)-i-1] : 
      return False;
  return True;

def findNum(n) : 
  start = findStart(n);

  for i in range(start, len(primes)) : 
    if isPalindrome(primes[i]) : 
      return primes[i];

getPrimes();
print(findNum(n));