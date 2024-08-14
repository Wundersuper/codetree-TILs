N, M = tuple(map(int, input().split()))

tile = [[0] * N for _ in range(N)]


def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N


dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1] #NESW

for i in range(M):
    r, c = tuple(map(int, input().split()))
    x, y = r-1, c-1

    tile[x][y] = 1
    cnt = 0
    for i in range(4):
        nx, ny = x + dxs[i], y + dys[i]
        if in_range(nx, ny) and tile[nx][ny] == 1:
            cnt += 1
    
    if cnt == 3:
        print('1') #편안한 상태
    else:
        print('0')