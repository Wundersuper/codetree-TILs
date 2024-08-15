N = int(input())
maps = [list(input()) for _ in range(N)]
K = int(input()) #레이저 쏘는 위치


def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N

#1~N: D, N+1~2N: L, 2N+1~3N: U, 3N+1~4N: R
#def start_info(n, k):
    #if 1 <= k <= n:
        #x, y, dir_num = 0, k-1, 1
    #elif (n+1) <= k <= 2*n:
        #x, y, dir_num = k-5, n-1, 2
    #elif (2*n+1) <= k <= 3*n:
        #x, y, dir_num = n-1, 3*n-k, 3
    #elif (3*n+1) <= k <= 4*n:
        #x, y, dir_num = 4*n-k, 0, 0

    #return x, y, dir_num


#x, y, dir_num = start_info(N, K)
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1] #DLUR

dir_num = 3
x, y = 0, 0
i = 1

# 시작 x, y 정하는 부분

while i < K:
    nx = x + dxs[dir_num]
    ny = y + dys[dir_num]

    if not in_range(nx, ny):
        i += 1
        dir_num = (dir_num + 1) % 4
        continue

    x, y = nx, ny
    i += 1

dir_num = (dir_num + 1) % 4

cnt = 0
while in_range(x, y):
    if maps[x][y] == '/':
        dir_num = (4 - dir_num + 1) % 4
        cnt += 1
    elif maps[x][y] == '\\':
        dir_num = 3 - dir_num
        cnt += 1

    x, y = x + dxs[dir_num], y + dys[dir_num]

print(cnt)