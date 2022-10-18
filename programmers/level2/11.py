def makeDict(word):
    cnt = 1
    order1 = {"A": 0, "E": 1, "I": 2, "O": 3, "U": 4}
    order2 = ["A", "E", "I", "O", "U"]

    cur = word[0]

    while cur != word:
        if len(cur) < 5:
            cur += "A"
        else:
            # 받아올림이 필요할 경우
            if cur[-1] == "U":
                i = 0
                while cur[len(cur) - i - 1] == "U":
                    i += 1
                cur = cur[: 4 - i] + order2[(order1[cur[-(i + 1)]] + 1) % 5]
            else:
                cur = cur[:4] + order2[(order1[cur[-1]] + 1) % 5]
        cnt += 1

    return cnt


def solution(word):
    answer = 0

    order = {"A": 0, "E": 1, "I": 2, "O": 3, "U": 4}

    first = word[0]

    # 해당 단어 앞에 몇 개의 숫자가 있는지
    before = order[first] * 781
    after = makeDict(word)

    answer = before + after

    return answer


word = "EIO"
print(solution(word))

"""
a
aa
aaa
aaaa

aaaaa
aaaae
aaaai
aaaao
aaaau

aaae
aaaea
aaaei
aaaeo
aaaeu

aaai
aaaia
aaaie
aaaii
aaaio
aaaiu

a로 시작하는 게 
625 * 125 + 25 + 5 + 1 = 781


e
ea
eea
eeea

eeeea
eeeee
eeeei
eeeeo
eeeeu

eeea
eeeaa
eeeae
eeeai
eeeao
eeeau

eeee
eeeea
eeeei
eeeeo
eeeeu

eeei
eeeia
eeeie
eeeii
eeeio
eeeiu

eeeu
eeeua
eeeue
eeeui
eeeuo
eeeuu

eei

"""
