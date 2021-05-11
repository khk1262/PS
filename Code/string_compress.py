def solution(string):
    result = 1e9
    if len(string) == 1:
        result = 1
    else:
        for i in range(1, len(string) // 2 + 1):
            li = []
            num = 1
            for j in range(0, len(string), i):

                if string[j:j+i] == string[j+i:j+2*i]:
                    num += 1
                else:
                    li.append((num, string[j:j+i]))
                    num = 1
            temp = ''
            for t in li:
                if t[0] != 1:
                    temp += (str(t[0]) + t[1])
                else:
                    temp += t[1]
            result = min(result, len(temp))
    return result

st = input()
print(solution(st))