N = int(input())

mapper = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3
}
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

x, y = 0, 0

cnt = 0
for i in range(N):
    d, f = input().split()
    dir_num = mapper[d]

    for j in range(int(f)):
        x, y = x + dxs[dir_num], y + dys[dir_num]
        cnt += 1
        if x == 0 and y == 0:
            print(cnt)
            exit(0)

if x != 0 and y != 0:
    print(-1)