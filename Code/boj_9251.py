A = input()
B = input()

lcs = [[0 for col in range(len(A) + 1)] for row in range(len(B) + 1)]

for i in range(1, len(B) + 1):
    for j in range(1, len(A) + 1):
        if A[j-1] == B[i-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs[len(B)][len(A)])

#  두 문자열의 LCS 출력부분
# for i in range(1, len(A) + 1):
#     if lcs[len(B)][i-1] < lcs[len(B)][i]:
#         print(A[i-1], end=' ')
