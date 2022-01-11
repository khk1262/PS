def solution(brown, yellow):
    answer = []

    for i in range(1, yellow+1):
        if yellow % i == 0:
            h = yellow // i
            if brown == (2*(h+2) + 2 * (i+2) - 4):
                answer.append(h+2)
                answer.append(i+2)
                break
    return answer


print(solution(24, 24))