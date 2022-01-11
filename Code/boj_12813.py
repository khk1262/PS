a = input()
b = input()

a_and_b = ''
a_or_b = ''
a_xor_b = ''
not_a = ''
not_b = ''

for i in range(len(a)):
    if a[i] == b[i]:
        a_and_b += a[i]
        a_or_b += a[i]
        a_xor_b += '0'
    else:
        a_and_b += '0'
        a_or_b += '1'
        a_xor_b += '1'

    if a[i] == '1':
        not_a += '0'
    else:
        not_a += '1'

    if b[i] == '1':
        not_b += '0'
    else:
        not_b += '1'

print(a_and_b)
print(a_or_b)
print(a_xor_b)
print(not_a)
print(not_b)