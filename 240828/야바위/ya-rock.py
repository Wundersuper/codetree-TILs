n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = 0
for i in range(1, 4): # 종이컵 1,2,3
    stone = [0] * 4
    cnt = 0
    for j in range(n):
        stone[i] += 1
        a, b, c = arr[j]
        if stone[a] == 1:
            stone[a] -= 1
            stone[b] += 1
        elif stone[b] == 1:
            stone[b] -= 1
            stone[a] += 1
        if stone[c] == 1:
            cnt += 1
    ans = max(ans, cnt)

print(ans)