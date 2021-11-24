import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        temp = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, temp)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return answer


print(solution([1, 2, 3, 9, 10, 12]	, 7))

# 이 문제에서 아주 잘 생각해야할 것은 힙 구조에서 만약 최소힙이라면 pop할때마다 가장 최소값이 나오는 것은 맞지만
# 값이 순서대로 들어가있지 않다.
# 내부에서 트리 구조가 맞춰가면서 저장하는 것, 정렬이 아닌

# import heapq
#
#
# temp = [1,23,3,4,5,6,7,2,8,11,35,763,5445,22,6,6,3,3,2,1]
# heapq.heapify(temp)
# print(temp)