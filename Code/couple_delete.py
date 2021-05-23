def solution(s):
    answer = 0
    temp = s[:]
    while True:
        check = False
        for i in range(1, len(temp)):
            if temp[i-1] == temp[i]:
                temp = temp[:i-1] + temp[i+1:]
                check = True
                break
        if not check:
            answer = 0
            break
        if not len(temp):
            answer = 1
            break
    return answer

a = input()

print(solution(a))