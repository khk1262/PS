def solution(s):
    answer = []

    temp1 = []
    temp2 = []
    str_int = ''
    count = 0
    for c in s:
        if c == '{':
            count += 1
        if count == 2 and c.isdigit():
            str_int += c

        if count == 2 and c == ',':
            temp2.append(int(str_int))
            str_int = ''
        if count == 2 and c == '}':
            count -= 1
            temp2.append(int(str_int))
            str_int = ''
            temp1.append(temp2[:])
            temp2 = []
    temp1.sort(key=len)

    for t in temp1:
        if not answer:
            answer.append(*t)
        else:
            answer.append(*(set(t)-set(answer)))
    return answer

s = input()

print(solution(s))