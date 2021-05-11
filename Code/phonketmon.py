def solution(nums):
    total = len(nums) // 2
    se_len = len(set(nums))
    answer = se_len if se_len <= total else total
    return answer


li = list(map(int, input().split()))

print(solution(li))