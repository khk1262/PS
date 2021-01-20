'''
성적순위가 공백을 두고 주어짐
이때 서류심사 성적을 기준으로 우선 정렬하고, 그 중 가장 높은 순위의 것을 뽑고,
해당 순위의 사람의 면접 성적을 기준으로 두고, 다음 서류심사 성적 기반의 다음 순번 사람의 면접 성적을
'''
import sys

for _ in range(int(sys.stdin.readline())):
    d = {}
    result = 0
    for _ in range(int(sys.stdin.readline())):
        a, b = map(int, sys.stdin.readline().split())
        d[a] = b
    sort_d = sorted(d.items(), key=lambda x: x[0])
    result += 1
    stand = sort_d[0][1]
    for i in range(1, len(sort_d)):
        if sort_d[i][1] < stand:
            result += 1
            stand = sort_d[i][1]

    print(result)
