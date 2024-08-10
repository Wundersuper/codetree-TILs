rects =[
    tuple(map(int, input().split()))
    for _ in range(2)
]

tile = [[0]*2001 for _ in range(2001)]
OFFSET = 1000

for i, (x1, y1, x2, y2) in enumerate(rects, start = 1):
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET

    for x in range(x1, x2):
        for y in range(y1, y2):
            tile[x][y] = i

min_x, max_x, min_y, max_y = 2000, 0, 2000, 0
first_rect_exist = False
for x in range(2001):
    for y in range(2001):
        if tile[x][y] == 1:
            first_rect_exist = True
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

if not first_rect_exist:
    area = 0
else:
    area = (max_x-min_x+1) * (max_y-min_y+1)

print(area)