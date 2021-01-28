def solution(record):
    answer = []

    c_dict = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    temp = []
    nick_dict = {}

    for i in record:
        c_line = i.split(' ')

        if c_line[0] == "Enter":
            temp.append((c_line[1], c_dict[c_line[0]]))
            nick_dict[c_line[1]] = c_line[2]
        elif c_line[0] == "Leave":
            temp.append((c_line[1], c_dict[c_line[0]]))
        else:
            nick_dict[c_line[1]] = c_line[2]

    for i in temp:
        answer.append(nick_dict[i[0]] + i[1])

    return answer


li = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]

print(solution(li))