cmd = list(input())

x, y = 0, 0
dir_num = 0
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0] #북서남동 0123

for i in range(len(cmd)):
    if cmd[i] == 'L':
        dir_num = (dir_num + 1) % 4
    elif cmd[i] == 'R':
        dir_num = (dir_num - 1 + 4) % 4
    elif cmd[i] == 'F':
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)