def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        answer += i if i ** (1/2) % 1 != 0 else -i

    return answer

print(solution(13, 17))