def solution(board, moves):
    answer = 0
    n = len(board[0])
    stack = [[]]
    bucket = []

    for i in range(n) : 
        stack.append([])
        for j in range(n) : 
            if board[j][i] == 0 : continue
            stack[i+1].insert(0, board[j][i])

    for move in moves : 
        if len(stack[move]) == 0 : continue

        popped = stack[move].pop()

        if len(bucket) > 0:
            if bucket[-1] == popped :  
                bucket.pop()
                answer += 2
            else : 
                bucket.append(popped)
        else : 
            bucket.append(popped)
    

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))