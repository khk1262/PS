def solution(cacheSize, cities):
    answer = 0
    cache = {}
    clock = 0

    for city in cities:
        clock += 1
        if len(cache) < 3:
            if city not in cache:
                answer += 5
                cache[city] = clock
            else:
                answer += 1
                cache[city] = clock
        else:
            if city not in cache:
                ex = min(cache, key=lambda x: cache[x])
                del cache[ex]
                answer += 5
                cache[city] = clock
            else:
                answer += 1
                cache[city] = clock

    return answer


print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
# print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))