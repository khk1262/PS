def solution(S, pattern):
    answer = 0
    s_len = len(S)
    p_len = len(pattern)
    pattern = sorted(pattern)


    for i in range(s_len - p_len + 1):
        temp = S[i:p_len+i]
        temp = sorted(temp)
        if temp == pattern:
            answer += 1

    return answer


print(solution("tegsornamwaresomran", "ransom"))