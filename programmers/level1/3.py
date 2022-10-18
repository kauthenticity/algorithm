def solution(arr):
    answer = []

    answer.append(arr[0])

    for i in range(1, len(arr)) : 
        prev = arr[i-1]
        cur = arr[i]

        if prev != cur : 
            answer.append(cur)

    return answer

arr = [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]

print(solution(arr))