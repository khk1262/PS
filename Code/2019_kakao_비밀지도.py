def binary(n, x):
    y=''
    while x>0:
        y=str(x%2)+y
        x//=2
    while len(y) < n:
        y = '0' + y
    return y


def solution(n, arr1, arr2):
    answer = []
    i = 0
    while i < n:
        a = binary(n, arr1[i])
        print(a)
        b = binary(n, arr2[i])
        print(b)
        result = ''
        for j in range(len(a)):
            if a[j] == '0' and a[j] == b[j]:
                result += ' '
            else:
                result += '#'
        answer.append(result)
        i += 1

    return answer


# 프로그래머스의 간략화된 풀이
# def solution(n, arr1, arr2):
#     answer = []
#     for i,j in zip(arr1,arr2):
#         a12 = str(bin(i|j)[2:])
#         print(a12)
#         a12=a12.rjust(n,'0')
#         a12=a12.replace('1','#')
#         a12=a12.replace('0',' ')
#         answer.append(a12)
#     return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))