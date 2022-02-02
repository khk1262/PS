def solution(name):
    answer = 0
    min_left_right = len(name) - 1 # 왼쪽에서 오른쪽으로만 이동할 때 좌,우 조작 횟수
    next_idx = 0

    # 마지막 A의 갯수들을 빼주어서 연산의 최소화를 해준다.
    # 마지막이 A로 끝나는 경우에는 그냥 오른쪽으로 쭉 가는 연산을 할때 len(name) - 1만큼 이동할 필요가 없음
    # 따라서 마지막 n개의 A를 빼줌으로, len(name) - n - 1
    while name[min_left_right] == 'A' and min_left_right > 0:
        min_left_right -= 1

    for idx, char in enumerate(name):
        # 위, 아래 조작 횟수의 최솟값 구하기
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 좌, 우 조작 횟수의 최솟값 구하기
        next_idx = idx + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1  # 현재 위치 이후 연속된 A 다음의 문자를 가리킴

        # 한 방향으로만 이동하는 경우와, 오른쪽으로 이동했다가 왼쪽으로 이동하는 경우를 비교
        min_left_right = min(min_left_right, idx + idx + len(name) - next_idx)
    answer += min_left_right
    return answer

print(solution("B"))