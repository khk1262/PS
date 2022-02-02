

def solution(n, m):
    answer = []

    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)

    temp = gcd(n,m)
    answer.append(temp)
    answer.append(n*m//temp)

    return answer


print(solution(3, 12))