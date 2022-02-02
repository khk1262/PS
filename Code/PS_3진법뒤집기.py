def solution(n):
    answer = 0
    temp = ''

    while n > 0:
        n, m = divmod(n, 3)
        temp += str(m)

    i = 0
    for j in range(len(temp)-1, -1, -1):
        answer += (int(temp[j]) * (3**i))
        i += 1

    return answer


print(solution(125))