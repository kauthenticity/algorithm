def calcDist(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    return abs(x2-x1) + abs(y2-y1)

    
def solution(numbers, hand):
    #keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [*, 0, #]]
    answer = ''
    curL = [3, 0]
    curR = [3, 2]
    
    for num in numbers : 
        if num == 1 or num==4 or num==7 :
            curL = [num//3,0]
            answer += 'L'
        elif num == 3 or num ==6 or num==9 :
            curR = [(num//3)-1,2]
            answer += 'R'
        else : 
            distL = 0
            distR = 0
            if num == 0 :
                distL = calcDist(curL, [3, 1])
                distR = calcDist(curR, [3, 1])
            else : 
                distL = calcDist(curL, [num//3,1])
                distR = calcDist(curR,  [num//3, 1])
            
            if distL < distR :
                answer += 'L'
                curL = [3, 1] if num == 0 else [num//3, 1]
            
            elif distL > distR : 
                answer += 'R'
                curR = [3, 1] if num == 0 else [num//3, 1]
            else : 
                if hand == 'right' : 
                    curR = [3, 1] if num == 0 else [num//3, 1]
                    answer += 'R'
                else : 
                    curL = [3, 1] if num == 0 else [num//3, 1]
                    answer += 'L'
        
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))

#res : "LRLLLRLLRRL"