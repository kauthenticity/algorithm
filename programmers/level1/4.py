def solution(sizes):
    answer = 0

    width = []
    height = []
    for size in sizes : 
        w, h = size
        if w >= h :
            width.append(w)
            height.append(h)
        else : 
            width.append(h)
            height.append(w)

    maxWidth = max(width)
    maxHeight = max(height)



    answer = maxWidth * maxHeight
    return answer

sizes =[[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]



print(solution(sizes))