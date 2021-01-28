def solution(str1, str2):
    answer = 0
    temp1 = []
    temp2 = []

    str1 = str1.lower();
    str2 = str2.lower()

    for i in range(1, len(str1)):
        if ((ord(str1[i - 1]) - ord('a')) >= 0 and (ord(str1[i - 1]) - ord('a')) <= 25) and (
                (ord(str1[i]) - ord('a')) >= 0 and (ord(str1[i]) - ord('a')) <= 25):
            temp1.append(str1[i - 1:i + 1])

    for i in range(1, len(str2)):
        if (ord(str2[i - 1]) - ord('a') >= 0 and ord(str2[i - 1]) - ord('a') <= 25) and (
                ord(str2[i]) - ord('a') >= 0 and ord(str2[i]) - ord('a') <= 25):
            temp2.append(str2[i - 1:i + 1])

    join_set = set(temp1) & set(temp2)
    union_set = set(temp1) | set(temp2)

    min_cnt = 0;
    max_cnt = 0

    for i in join_set:
        min_cnt += min(temp1.count(i), temp2.count(i))

    for i in union_set:
        max_cnt += max(temp1.count(i), temp2.count(i))

    if min_cnt == 0 and max_cnt == 0:
        answer = 1 * 65536
    else:
        answer = int(min_cnt / max_cnt * 65536)

    return answer