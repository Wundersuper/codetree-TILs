n, t = tuple(map(int, input().split()))

r, c, d = tuple(input().split())
r, c = int(r), int(c)

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1] 
mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


x, y = r-1, c-1
c_dir = d
move_dir = mapper[c_dir]

for i in range(t):
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    if not in_range(nx, ny):
        move_dir = 3 - move_dir
    else:
        x, y = nx, ny
    


print(x+1, y+1)