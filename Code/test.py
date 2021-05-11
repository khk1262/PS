def solution(purchase):
    month = {'02': 31, '03': (28+31), '04': (31+28+31), '05': (30+31+28+31), '06': (31+30+31+28+31),
             '07': (30+31+30+31+28+31), '08': (31+30+31+30+31+28+31), '09': (31+31+30+31+30+31+28+31),
             '10': (30+31+31+30+31+30+31+28+31), '11': (31+30+31+31+30+31+30+31+28+31),
             '12': (30+31+30+31+31+30+31+30+31+28+31), '01': 0}
    answer = [0, 0, 0, 0, 0]
    tt = [0] * 366
    index = 0

    for i in purchase:
        a, b = i.split(' ')
        money = int(b)
        temp = list(a.split('/'))
        day = month[temp[1]] + int(temp[2])
        if (day + 30) <= month['12'] + 31:
            for j in range(day, day + 30):
                tt[j] += money
        else:
            for j in range(day, 366):
                tt[j] += money

    for t in range(1, len(tt)):
        if tt[t] != tt[t-1]:
            if 0 <= tt[t] < 10000:
                index = 0
            elif 10000 <= tt[t] < 20000:
                index = 1
            elif 20000 <= tt[t] < 50000:
                index = 2
            elif 50000 <= tt[t] < 100000:
                index = 3
            else:
                index = 4
        answer[index] += 1
    return answer


print(solution(["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000"]))