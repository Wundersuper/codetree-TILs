A = list(input())

ans = 0
for i in range(len(A)-2):
    for j in range(i+2, len(A)-2):
        if A[i] + A[i+1] == '((' and A[j] + A[j+2] == '))':
            ans += 1

print(ans)