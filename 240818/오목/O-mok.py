n = 19
tile = [
    list(map(int, input().split()))
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def check_win(x, y, dx, dy, cur):
    for i in range(1, 5):
        nx, ny = x + i * dx, y + i * dy
        if not in_range(nx, ny) or tile[nx][ny] != cur:
            return False
    return True


def find_winner():
    for x in range(n):
        for y in range(n):
            if tile[x][y] == 1 or tile[x][y] == 2:
                # 오른쪽, 아래, 오른대각선, 왼대각선
                dxs, dys = [0, 1, 1, 1], [1, 0, 1, -1]
                for dx, dy in zip(dxs,dys):
                    if check_win(x, y, dx, dy, tile[x][y]):
                        return tile[x][y], x + dx * 2, y + dy * 2
    
    return 0, None, None


winner, x, y = find_winner()
if winner:
    print(winner)
    print(x + 1, y + 1)
else:
    print(0)