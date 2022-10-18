def solution(survey, choices):
  answer=''

  score = {
    'R' : 0,
    'T' : 0,
    'C' : 0,
    'F' : 0,
    'J' : 0,
    'M' : 0,
    'A' : 0,
    'N' : 0,
  }

  for i in range(len(survey)) : 
    t1, t2 = survey[i]
    choice = choices[i]

    if choice < 4 : 
      score[t1] += choice
    else : 
      score[t2] += choice

  answer += 'R' if score['R'] >= score['T'] else 'T'
  answer += 'C' if score['C'] >= score['F'] else 'F'
  answer += 'J' if score['J'] >= score['M'] else 'M'
  answer += 'A' if score['A'] >= score['N'] else 'N'


  return answer

survey= ["AN"]	
choices =	[7]
print(solution(survey, choices))