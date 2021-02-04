import heapq
import sys

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    a = int(input())
    if a < 0:
        heapq.heappush(heap, (abs(a) - 0.5, a))
    elif a > 0:
        heapq.heappush(heap, (a, a))
    else:
        print(heapq.heappop(heap)[1]) if heap else print(0)
