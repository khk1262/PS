from itertools import combinations


def solution(numbers):
    answer = sorted(list(set(map(sum, combinations(numbers, 2)))))
    return answer


print(solution([2,1,3,4,1]))