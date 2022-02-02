position = [[3,1],
            [0,0], [0,1], [0,2],
            [1,0], [1,1], [1,2],
            [2,0], [2,1], [2,2],
            [3,0], [3,2]]

hands = ['N', 'L', 'N', 'R', 'L', 'N', 'R', 'L', 'N', 'R']


def solution(numbers, hand):
    answer = ''
    left = 10
    right = 11

    for number in numbers:
        if hands[number] == 'N':
            if abs(position[number][0] - position[left][0]) + abs(position[number][1] - position[left][1]) < \
                    abs(position[number][0] - position[right][0]) + abs(position[number][1] - position[right][1]):
                left = number
                answer += 'L'
            elif abs(position[number][0] - position[left][0]) + abs(position[number][1] - position[left][1]) > \
                    abs(position[number][0] - position[right][0]) + abs(position[number][1] - position[right][1]):
                right = number
                answer += 'R'
            else:
                if hand == 'right':
                    right = number
                    answer += 'R'
                else:
                    left = number
                    answer += 'L'

        elif hands[number] == 'R':
            right = number
            answer += 'R'

        else:
            answer += 'L'
            left = number
    return answer


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))