n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1] #북동남서 0123


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


cnt_one = 0


for i in range(n):
    for j in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            x, y = i, j
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and arr[nx][ny] == 1:
                cnt += 1
        
        if cnt >= 3:
            cnt_one += 1

print(cnt_one)