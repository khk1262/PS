from collections import Counter
from itertools import combinations
import sys
input = sys.stdin.readline


def solution(orders, course):
    answer = []

    for num in course:
        temp_answer = []
        for st in orders:
            temp = list(map(list, combinations(sorted(st), num)))
            temp_answer += temp
        temp_answer = list(map("".join, temp_answer))

        if temp_answer:
            c = Counter(temp_answer).most_common()
            most = c[0][1]
            for element in c:
                if 1 < most == element[1]:
                    answer.append(element[0])
                else:
                    break
    answer.sort()
    return answer


orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

print(solution(orders, course))




'''
더 간단한 코드
def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]
'''