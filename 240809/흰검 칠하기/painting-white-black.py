n = int(input())

tile = [0] * 200001
white, black = [0] * 200001, [0] * 200001
start = 10000

for i in range(n):
    move, direction = tuple(input().split())
    move = int(move)

    if direction == 'L':
        for j in range(start-move+1, start+1):
            tile[j] = 1
            white[j] += 1
        start -= move-1
    else:
        for j in range(start, start+move):
            tile[j] = 2
            black[j] += 1
        start += move-1

w, b, g = 0, 0, 0
for i in range(len(tile)):
    if white[i] >= 2 and black[i] >= 2:
        g += 1
    elif tile[i] == 1:
        w += 1
    elif tile[i] == 2:
        b += 1

print(w, b, g)