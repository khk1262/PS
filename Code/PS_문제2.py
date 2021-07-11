
dic = ['A', 'E','I', 'O', 'U']

def solution(value):
    answer = 1
    check = 'A'
    word = [0]
    while check != value:
        if word[-1] == 4:
            word.pop()
            answer += 1
        else:
            word[-1] += 1
            answer += 1
        temp = ''
        for i in word:
            temp += dic[i]
        check = temp

        if check == value:
            break
        if len(word) < 5:
            word.append(0)

    return answer


print(solution("AAAAE"))


def solution(letters, k):
    answer = ''
    temp = letters[:]
    i = 0

    while len(temp) > k:
        answer = temp

        temp = temp.replace(chr(97 + i), '')
        i += 1
        print(temp)
    print(temp)
    answer = temp[:k] if len(temp) >= k else answer[:k]
    return answer
#
#
# print(solution("aaaaka"	, 3))