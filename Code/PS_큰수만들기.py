# def solution(number, k):
#     numbers = list(map(int, number))
#     n = len(numbers)
#     temp = numbers[:n - k]
#
#     for i in range(n-k, n):
#         t = numbers[i]
#         s = 0
#         for j in range(1, n-k):
#             if temp[j] > temp[j-1]:
#                 s = j
#                 break
#         if s:
#             temp = temp[:s-1] + temp[s:]
#             temp.append(t)
#         else:
#             if temp[-1] < t:
#                 temp[-1] = t
#     answer = ''.join(map(str, temp))
#     return answer
def solution(number, k):
    collected = []

    for (i, num) in enumerate(number):
        while collected and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1

        if k == 0:
            collected += number[i:]
            break

        collected.append(num)

    collected = collected[:-k] if k > 0 else collected
    answer = "".join(collected)
    return answer

print(solution("4177252841"	, 4))