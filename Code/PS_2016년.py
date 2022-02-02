day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def solution(a, b):
    answer = ''
    total = 0
    for i in range(a):
        total += days[i]
    total += b
    total -= 1
    answer = day[total % 7]

    return answer

print(solution(5, 24))