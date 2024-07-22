n = int(input())

arr = list(map(int, input().split()))

ans = [elem ** 2 for elem in arr]

for i in range(n):
    print(ans[i], end = " ")