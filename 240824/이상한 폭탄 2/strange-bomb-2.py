n, k = tuple(map(int, input().split()))
bombs = [int(input()) for _ in range(n)]

max_num = -1
for i in range(n):
    for j in range(i+1, n):
        if j - i <= k and bombs[i] == bombs[j]:
            max_num = max(max_num, bombs[i])

print(max_num)