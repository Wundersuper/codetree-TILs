N = int(input())

tile = [[0] * 201 for _ in range(201)]
OFFSET = 100

for i in range(N):
    x1, y1, x2, y2 = tuple(map(int, input().split()))

    x1, y1 = x1+OFFSET, y1+OFFSET
    x2, y2 = x2+OFFSET, y2+OFFSET

    for x in range(x1, x2):
        for y in range(y1, y2):
            tile[x][y] = 1

area = 0
for x in range(0, 201):
    for y in range(0, 201):
        if tile[x][y] == 1:
            area += 1

print(area)