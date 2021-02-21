import sys

input = sys.stdin.readline
id_list = [chr(ord('a') + i) for i in range(26)] + [chr(ord('0') + i) for i in range(10)] + ['-', '_', '.']


def remove_sign(s):
    temp = ''
    for i in range(len(s)):
        if s[i] in id_list:
            temp += s[i]
    return temp


def remove_dot(s):
    temp = ''
    dot_cnt = 0
    for i in range(len(s)):
        if s[i] == '.':
            dot_cnt += 1
        else:
            dot_cnt = 0
        if dot_cnt < 2:
            temp += s[i]

    if len(temp) == 1 and temp[0] == '.':
        temp = ''
    elif len(temp) > 1:
        if temp[0] == '.':
            temp = temp[1:]
        if temp[-1] == '.':
            temp = temp[:-1]
    return temp


def solution(new_id):
    answer = ''
    temp = new_id.lower()
    temp = remove_sign(temp)
    temp = remove_dot(temp)

    if len(temp) == 0:
        answer += 'a'
    else:
        answer += temp

    answer_len = len(answer)

    if answer_len >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    elif answer_len <= 2:
        answer += (answer[-1] * (3 - answer_len))
    return answer


n_id = input().rstrip()
print(solution(n_id))

