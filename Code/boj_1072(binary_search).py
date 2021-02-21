'''
99%는 절대로 100%가 될 수 없다는 것을 명심

'''

import sys

input = sys.stdin.readline

#upper bound
def b_search(x, y):
    start, end = 0, y # 현재까지 주어진 분모의 크기만큼만 주어도 값이 나옴
    target = int(x * 100 / y)

    if target >= 99:
        return -1
    while start < end:
        mid = (start + end) // 2
        temp = int((x+mid) * 100 / (y+mid))
        if target < temp:
            end = mid
        else:
            start = mid + 1
    return start


X, Y = map(int, input().split())
print(b_search(Y, X))
