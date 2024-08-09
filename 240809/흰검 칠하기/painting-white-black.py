n = int(input())

tile = [0] * 200001
white, black = [0] * 200001, [0] * 200001
start = 10000

for i in range(n):
    move, direction = tuple(input().split())
    move = int(move)

    if direction == 'L':
        #for j in range(start-move+1, start+1):
        for j in range(1, move+1):
            tile[start - j] = 1
            white[start - j] += 1
        start -= move
    else:
        #for j in range(start, start+move):
        for j in range(move):
            tile[start+j] = 2
            black[start+j] += 1
        start += move

w, b, g = 0, 0, 0
for i in range(len(tile)):
    if white[i] >= 2 and black[i] >= 2:
        g += 1
    elif tile[i] == 1:
        w += 1
    elif tile[i] == 2:
        b += 1

print(w, b, g)