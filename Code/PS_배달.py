import heapq
INF = int(1e9)

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)]

    for r in road:
        graph[r[0]].append((r[1], r[2]))
        graph[r[1]].append((r[0], r[2]))

    def dijkstra(start):
        distance = [INF] * (N + 1)
        hq = []
        distance[start] = 0
        heapq.heappush(hq, (0, start))
        while hq:
            cur_dist, cur_node = heapq.heappop(hq)
            if distance[cur_node] < cur_dist:
                continue
            for next_node, next_dist in graph[cur_node]:
                dist = cur_dist + next_dist
                if dist < distance[next_node]:
                    distance[next_node] = dist
                    heapq.heappush(hq, (dist, next_node))
        return distance[1:]
    li = dijkstra(1)

    for i in li:
        if i <= K:
            answer += 1
    return answer


print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))