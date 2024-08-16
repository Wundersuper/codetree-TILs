N, T = tuple(map(int, input().split()))
cmd = list(input())

tile = [
    list(map(int, input().split()))
    for _ in range(N)
]


def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N


dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1] #ULDR
x, y, dir_num = N//2, N//2, 0

sum_val = tile[x][y]
for elem in cmd:
    if elem == 'L':
        dir_num = (dir_num + 1) % 4
    elif elem == 'R':
        dir_num = (dir_num + 4 - 1) % 4
    elif elem == 'F':
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        if not in_range(nx, ny):
            continue
        else:
            x, y = nx, ny
            sum_val += tile[x][y]

print(sum_val)