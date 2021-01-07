'''
단순히 생각해서 자연수의 합 S가 될수 있는 최대의 개수 N을 구하는 것이므로
가장 작은 수 1부터 시작해서 더해 나가다 S보다 커지면 지금까지의 개수 중 1개를 빼준다
'''

S = int(input())

i = 1
sum = 0
num = 0
while True:
    num += 1
    sum+=i
    if sum > S:
        print(num-1)
        break
    i+=1
