from itertools import combinations

def prime_list(li):
    sum_li = sum(li)
    prime = [False, False] + [True] * (sum_li - 1)
    for i in range(2, sum_li+1):
        for j in range(i*2, sum_li+1, i):
            if prime[j] is True:
                prime[j] = False
    return prime


def solution(nums):
    answer = 0
    prime_li = prime_list(nums)

    com_li = list(map(sum, combinations(nums, 3)))

    for i in com_li:
        if prime_li[i]:
            answer += 1
    return answer


li = list(map(int, input().split()))
print(solution(li))

