# 최대공약수, 최소공배수가 문제에 나오면 제일 먼저 gcd, 즉 유클리드 호제법을 먼저 생각

def solution(arr):
    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)
    answer = arr[0]

    for i in range(1, len(arr)):
        answer = (answer*arr[i])//gcd(answer, arr[i])

    return answer


print(solution([2,6,8,14]))