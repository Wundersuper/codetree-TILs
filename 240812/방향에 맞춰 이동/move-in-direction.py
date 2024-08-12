N = int(input())

x, y = 0, 0
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0] #W, S, N, E

for i in range(N):
    direct, move = tuple(input().split())
    move = int(move)

    if direct == 'W':
        x, y = x + dx[0] * move, y + dy[0] * move
    elif direct == 'S':
        x, y = x + dx[1] * move, y + dy[1] * move
    elif direct == 'N':
        x, y = x + dx[2] * move, y + dy[2] * move
    else:
        x, y = x + dx[3] * move, y + dy[3] * move

print(x, y)