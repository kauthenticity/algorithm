def solution(id_list, report, k):
    answer = []

    # key : 신고당한 사람, value : key를 신고한 사라들의 list
    reporter = dict()

    # key : 신고당한 사람, value : 신고당한 횟수
    score = dict()

    for i in range(len(id_list)) : 
      answer.append(0)
      reporter[id_list[i]] = []
      score[id_list[i]] = 0
    
    for r in report : 
      r1, r2 = r.split(' ')

      # r1이 이미 r2를 신고한 적이 있으면 넘어감
      if reporter[r2] and r1 in reporter[r2] : 
        continue
      
      # r2를 신고한 사람에 r1을 추가하고 신고 횟수를 1 더함
      reporter[r2].append(r1)
      score[r2] += 1

    for key in reporter.keys() : 
      if score[key] >= k : 
        for person in reporter[key] : 
          answer[id_list.index(person)] += 1


    return answer

id_list=["muzi", "frodo", "apeach", "neo"]
report=["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k=2

print(solution(id_list,report, k))