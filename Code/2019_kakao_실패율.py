def solution(N, stages):
    answer = []
    cur = 0
    prev = 0
    stage = 1
    stages.sort()
    m = len(stages)

    while stage <= N:
        while cur < len(stages) and stages[cur] == stage:
            cur += 1
        cnt = cur - prev
        total = m - prev
        prev = cur

        if total == 0:
            answer.append((stage, 0))
        else:
            answer.append((stage, cnt / total))
        stage += 1
    answer.sort(key=lambda x : x[1], reverse=True)

    return [i[0] for i in answer]


print(solution(4, [4,4,4,4]))