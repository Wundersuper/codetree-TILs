move = list(input())

dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0] #NWSE
x, y = 0, 0
dir_num = 0
elapsed_time = 0

ans = -1
for elem in move:
    if elem == 'F':
        x, y = x + dxs[dir_num], y + dys[dir_num]
    elif elem == 'L':
        dir_num = (dir_num + 1) % 4
    elif elem == 'R':
        dir_num = (dir_num - 1 + 4) % 4

    elapsed_time += 1

    if x == 0 and y == 0:
        ans = elapsed_time
        break

print(ans)