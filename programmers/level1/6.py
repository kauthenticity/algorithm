def solution(new_id):
    answer = ''

    # 생성 과정
    # 1. 대문자 -> 소문자
    # 2. 가능한 문자 제외 제거
    # 3. 연속된 마침표를 하나의 마침표로 변환
    # 4. 마침표가 처음이나 끝에 있으면 제거
    # 5. 빈 문자열이면 "a"로 치환
    # 6. 5단계까지 했는데 16자 이상이면 15자만 남기고 이렇게 했는데 끝에 (.) 있으면 제거
    # 7. 6단계까지 했는데 2자 이하라면 마지막 글자를 계속 붙힘.

    # print convention 
    # 1단계 변화 없습니다.
    # 7단계 "z-" → "z--"

    # 1단계
    answer = new_id.lower()
    if answer != new_id : 
        print('1.', '"'+new_id+'"', '->', '"'+answer+'"')
    else : 
        print('1단계 변화 없습니다.')
    new_id = answer

    # 2단계
    answer = ''
    for letter in new_id : 
        if (letter >= 'a' and letter <= 'z') or letter == '.' or letter == '_' or letter=='-' : 
            answer += letter

    if answer != new_id : 
        print('2.', '"'+new_id+'"', '->', '"'+answer+'"')
    else : 
        print('2단계 변화 없습니다.')
    new_id = answer

    # 3단계
    answer = new_id[0]

    for i in range(1, len(new_id)) : 
        if new_id[i] == '.' and new_id[i-1] == '.' : 
            continue
        else : 
            answer += new_id[i]

    if answer != new_id : 
        print('3.', '"'+new_id+'"', '->', '"'+answer+'"')
    else : 
        print('3단계 변화 없습니다.')
    new_id = answer

    # 4단계
    answer = ''

    temp = new_id
    new_id_len = len(new_id)
    if new_id == '.' : 
        new_id.pop(0)
    
    if new_id[new_id_len-1] == '.' : 
         new_id.pop(new_id_len-1)

    answer = new_id

    if answer != temp : 
        print('4.', '"'+temp+'"', '->', '"'+answer+'"')
    else : 
        print('4단계 변화 없습니다.')
    new_id = answer


    return answer

new_id='...!@BaT#*..y.abcdefghijklm'
print(solution(new_id))