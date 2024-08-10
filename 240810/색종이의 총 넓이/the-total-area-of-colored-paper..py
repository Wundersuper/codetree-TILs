N = int(input())

square = [
    tuple(map(int, input().split()))
    for _ in range(N)
]

tile = [[0] * 201 for _ in range(201)]
OFFSET = 100

for x1, y1 in square:
    x1, y1 = x1+OFFSET, y1+OFFSET

    for x in range(x1, x1+8):
        for y in range(y1, y1+8):
            tile[x][y] = 1

area = 0
for x in range(0, 201):
    for y in range(0, 201):
        if tile[x][y] == 1:
            area += 1

print(area)