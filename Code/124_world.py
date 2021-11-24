def recur(n, ans):
    frame = '4124'
    div, mod = divmod(n, 3)

    if mod == 0:
        div -= 1
        mod += 3

    ans = frame[mod] + ans

    if div > 0:
        return recur(div, ans)
    else:
        return ans


def solution(n):
    answer = ''
    return recur(n, answer)


n = int(input())
print(solution(n))
