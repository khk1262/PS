def solution(n, lost, reserve):
    answer = 0
    i = 0

    temp_reserve = list(set(reserve) - set(lost))
    temp_lost = list(set(lost) - set(reserve))

    l = len(temp_lost)

    for t in temp_lost:
        for p in temp_reserve:
            if t-1 == p or t+1 == p:
                i+=1
                temp_reserve.pop(temp_reserve.index(p))

    answer = n - l + i

    return answer

print(solution(5, [5,3],[1,2]))