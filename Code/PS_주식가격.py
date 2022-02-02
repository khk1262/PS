# def solution(prices):
#     stack = []
#     n = len(prices)
#     answer = [0] * n
#
#     for i in range(n):
#         j = i - 1
#         t = 1
#
#         while j >= 0:
#             if stack[j] <= 0:
#                 t += 1
#                 j -= 1
#             else:
#                 if stack[j] > prices[i]:
#                     stack[j] = -t
#                     t += 1
#                     j -= 1
#                 else:
#                     break
#         stack.append(prices[i])
#
#     temp = 0
#     for i in range(n-1, -1, -1):
#         if stack[i] > 0:
#             answer[i] = temp
#         else:
#             answer[i] = -stack[i]
#         temp += 1
#
#     return answer

from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer


print(solution([8, 2, 3, 1, 3, 2, 3, 9, 4, 2, 6, 1, 2, 4, 6]))