def solution(li):
    stack = []
    prev = 0
    result = 0
    for i in li:
        if i > prev:
            stack.append(i)
        else:
            result = max(result, stack[-1] - stack[0])
            stack.clear()
            stack.append(i)
        prev = i
    result = max(result, stack[-1] - stack[0])

    return result


N = int(input())
li = list(map(int, input().split()))

print(solution(li))