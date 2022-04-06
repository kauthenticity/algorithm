dp = [0, 0, 1, 1];

def make1(n) : 
  counter = 0;

  for i in range (4, 1000001) :
    counter += 1;
    # 무조건 현재 수에서 1을 빼서 전의 수로 1을 만들 수 있음
    dp.append(dp[i-1]+1)

    # 3의 배수. %3 연산 시간을 줄이기 위해 conter 사용
    if counter == 3 :
      dp[i] = min(dp[i//3]+1, dp[i]);
      counter = 0;
    # 2의 배수
    if i%2 == 0 :
      dp[i] = min(dp[i//2] + 1, dp[i]);

  return dp[n];

n = int(input());

print(make1(n));