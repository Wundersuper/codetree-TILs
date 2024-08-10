n = int(input())

tile = [0] * 200001
start = 10000
#white: True, black: False

for i in range(n):
    move, direction = tuple(input().split())
    move = int(move)

    if direction == 'L':
        for j in range(start-move+1, start+1):
            tile[j] = 'True'
        start -= move-1
    else:
        for j in range(start, start+move):
            tile[j] = 'False'
        start += move-1

w, b = 0, 0
for i in range(len(tile)):
    if tile[i] == 'True':
        w += 1
    elif tile[i] == 'False':
        b += 1

print(w, b)