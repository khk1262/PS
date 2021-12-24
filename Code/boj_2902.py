t = list(input().strip())
result = ''
for i in t:
    if 0 <= ord(i) - ord('A') <= 25:
        result += i
print(result)

'''
a = list(input().split('-'))
for i in a:
    print(i[0], end = '')
    '''