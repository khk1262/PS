import sys

input = sys.stdin.readline


def check(s):
    total = 0
    i = 0
    correct = True

    while i <= len(s) - 1:
        if s[i] == '(':
            total += 1
        elif s[i] == ')':
            total -= 1

        if total < 0:
            correct = False
            break

        i += 1
    return correct


def divide(s):
    total = 0
    i = 0
    while True:
        if s[i] == '(':
            total += 1
        elif s[i] == ')':
            total -= 1

        if total == 0:
            break

        i += 1
    return s[:i+1], s[i+1:]


def convert(s):
    new = ''
    new += '('
    for i in range(1, len(s) - 1):
        if s[i] == '(':
            new += ')'
        elif s[i] == ')':
            new += '('
    new += ')'
    return new


def recursion_make(w):
    if w == '' or check(w):
        return w

    u, v = divide(w)
    if check(u):
        return u + recursion_make(v)
    else:
        return '(' + recursion_make(v) + ')' + convert(u)


def solution(p):
    answer = ''
    try:
        if check(p):
            answer += p
        else:
            answer += recursion_make(p)
    except Exception as e:
        print("예외발생", e)
    finally:
        return answer


string = input().rstrip()
print(solution(string))