def solution(d, budget):
    d.sort()
    cnt = 0
    total = 0
    for i in range(len(d)):
        total += d[i]
        if total <= budget:
            cnt += 1
        else:
            break
    return cnt


print(solution([1,3,2,5,4], 9))