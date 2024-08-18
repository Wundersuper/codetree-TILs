A = list(input())

ans = 0
for i in range(len(A)-3):
    for j in range(i+2, len(A)-1):
        if A[i] + A[i+1] == '((' and A[j] + A[j+1] == '))':
            ans += 1

print(ans)