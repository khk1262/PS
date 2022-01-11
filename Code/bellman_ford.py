import sys

input = sys.stdin.readline
INF = int(1e9)


def bf(start):
    dist[start] = 0

    # n번 반복, 원래는 n-1만으로 시작노드에서 끝 노드까지 다 되지만 음수 순환확인을 위한 마지막 한번 추가
    for i in range(n):
        # 모든 간선 반복, 이러면 최악의 사태가 발생해도 반드시 dist 값들은 모두 최단 거리를 담고 있게 됨
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # 현재 노드까지의 거리가 무한대이면 이후의 간선은 의미가 없어지므로 != INF 체크 먼저
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                if i == n - 1:
                    return True
    return False


n, m = map(int, input().split())
edges = []
dist = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

negative_cycle = bf(1)

if negative_cycle:
    print('-1')
else:
    for i in range(2, n+1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])

