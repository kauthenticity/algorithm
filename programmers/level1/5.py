def solution(lottos, win_nums):
    answer = []
    
    # numZero + match가 일치하는 횟수
    numZero = 0
    match = 0

    for lotto in lottos : 
        if lotto == 0 :
            numZero += 1
            continue
        if lotto in win_nums : 
            match += 1
    
    # 최대 6등인 경우
    if numZero + match < 2 : 
        answer = [6, 6]
    # 최대 1, 2, 3, 4, 5 등
    else : 
        # 최소 5등인 경우
        if match >= 2 : 
            answer = [7-numZero-match, 7-match]
        else : 
            answer = [7-numZero-match, 6]               
            
    return answer

lottos =[0, 0, 0, 0, 0, 0]
win_nums=[38, 19, 20, 40, 15, 25]

print(solution(lottos, win_nums))