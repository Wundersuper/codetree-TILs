N = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

max_coin = 0
for i in range(N):
    for j in range(N-2):
        max_coin = max(max_coin, arr[i][j] + arr[i][j+1] + arr[i][j+2])

print(max_coin)