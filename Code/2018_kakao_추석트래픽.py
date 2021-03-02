import sys
input = sys.stdin.readline

def make_list(line):
    li = list(map(str, line.split()))
    time = list(li[1].split(':'))
    print(time)
    total = float(''.join(time))
    print(total)

def solution(lines):
    answer = 0
    for line in lines:
        make_list(line)
    return answer

temp = [
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]

solution(temp)