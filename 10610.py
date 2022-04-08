from re import L


n = input()

def get30() : 
  digits = [];
  # 애초의 10의 배수로 못 만들기 때문에 30의 배수도 못 만듦.
  if len(n) > 1 and n.find('0') == -1 : 
    return -1;

  # 각 자릿수의 합이 3의 배수여야만 30의 배수임.
  sum = 0;
  for i in range(len(n)) :
    sum += int(n[i]);
    digits.append(n[i]);

  if sum%3 != 0 :
    return -1;
  
  # 이제 무조건 3의 배수니깐 각 자릿수 숫자 큰 순서대로 정렬만 하면 됨.
  digits.sort(reverse=True);
  digits = ''.join(digits);
  return digits;



ans = get30();
print(ans);