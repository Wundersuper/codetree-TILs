n, m = tuple(map(int, input().split()))
tile = [[0] * m for _ in range(n)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] #RDLU


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


x, y, dir_num = 0, 0, 0
alphabet = ord('A')
tile[x][y] = chr(alphabet)

for i in range(2, n*m+1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if not in_range(nx, ny) or tile[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
    
    x, y = x + dxs[dir_num], y + dys[dir_num]
    alphabet += 1
    tile[x][y] = chr(alphabet)
    if ord(tile[x][y]) > ord('Z'):
        tile[x][y] = chr(alphabet)

for i in range(n):
    for j in range(m):
        print(tile[i][j], end = ' ')
    print()