import sys

input = sys.stdin.readline



def find_all(s):
    len_s = len(s)
    mid = len_s // 2
    result = s[:]
    li = []
    for i in range(1, mid + 1):
        cnt = 1
        temp = ''
        check = s[:i]
        li.append(check)
        for j in range(i, len_s - i, i):
            if j <= len_s - i:
                if check == s[j: j + i]:
                    cnt += 1
                else:
                    if cnt > 1:
                        li.pop()
                        li.append(str(cnt))
                        li.append(check)
                        cnt = 1
                        check = s[j : j + i]
                    else:
                        li.append(s[j:j+i])
                        check = s[j : j + i]

            else:



        print(temp)
        result = temp if len(result) > len(temp) else result

    return result


def solution(s):
    answer = len(find_all(s))
    return answer


s = input().rstrip()

print(solution(s))