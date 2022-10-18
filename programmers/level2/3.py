import math


def solution(fees, records):
    answer = []  # 차 번호가 작은 순으로 주차 요금 출력

    feeDict = dict()

    defaultTime, defaultFee, overTime, overFee = fees

    for record in records:
        time, number, status = record.split(" ")

        if number not in feeDict.keys():
            feeDict[number] = []

        feeDict[number].append(time + " " + status)

    # 자동차 번호 오름차순으로 dictionary 정렬
    feeList = sorted(feeDict.items())

    for feeListItem in feeList:
        values = feeListItem

        if len(values[1]) % 2 == 1:
            values[1].append("23:59 OUT")

        diffSum = 0
        for i in range(0, len(values[1]), 2):
            inTime = values[1][i].split(" ")[0]
            outTime = values[1][i + 1].split(" ")[0]

            inHour, inMinute = map(int, inTime.split(":"))
            outHour, outMinute = map(int, outTime.split(":"))

            diff = (outHour * 60 + outMinute) - (inHour * 60 + inMinute)
            diffSum += diff

        if diffSum > defaultTime:
            answer.append(
                defaultFee + (overFee * math.ceil((diffSum - defaultTime) / overTime))
            )
        else:
            answer.append(defaultFee)

    return answer


fees = [180, 5000, 10, 600]  # 기본 시간, 기본 요금, 오버 시간 단위, 오버 단위 요금
records = [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT",
]

print(solution(fees, records))
