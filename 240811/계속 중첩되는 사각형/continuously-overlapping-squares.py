n = int(input())

rects = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

tile = [[0] * 201 for _ in range(201)]
OFFSET = 100

# 빨간색 = 1, 파란색 = 2
for i, (x1, y1, x2, y2) in enumerate(rects, start = 1):
    x1, y1 = x1+OFFSET, y1+OFFSET
    x2, y2 = x2+OFFSET, y2+OFFSET

    for x in range(x1, x2):
        for y in range(y1, y2):
            if i % 2 != 0:
                tile[x][y] = 1
            else:
                tile[x][y] = 2

area = 0
for x in range(0, 201):
    for y in range(0, 201):
        if tile[x][y] == 2:
            area += 1
        
print(area)