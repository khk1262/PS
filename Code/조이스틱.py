def cur(name, ver, ver_count, answer):

    if name[ver] != 'A':


        temp = min(ord(name[ver]-ord('A')), ord('Z')-ord(name[ver])+1)



    return



def solution(name):
    answer = 0

    for t in name:
        temp = ord(t) - ord('A')
        answer += temp if temp < 26 - temp else 26 - temp
        if t != 'A':
            answer += 1
    answer -= 1
    return answer

print(solution("JEROEN"))