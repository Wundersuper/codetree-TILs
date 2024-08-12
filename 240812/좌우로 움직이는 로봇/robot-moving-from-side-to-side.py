n, m = tuple(map(int, input().split()))

loc_a = [0] * 1000001
loc_b = [0] * 1000001

cur_loc, time_a = 1000001, 0
for i in range(n):
    t, d = tuple(input().split())
    t = int(t)

    if d == 'L':
        for _ in range(t):
            time_a += 1
            cur_loc -= 1
            loc_a[time_a] = cur_loc
    elif d == 'R':
        for _ in range(t):
            time_a += 1
            cur_loc += 1
            loc_a[time_a] = cur_loc
#움직임 종료 후에는 같은 위치에 계속 머물러있음
for i in range(time_a + 1, 1000001):
    loc_a[i] = cur_loc

cur_loc, time_b = 1000001, 0
for i in range(m):
    t, d = tuple(input().split())
    t = int(t)

    if d == 'L':
        for _ in range(t):
            time_b += 1
            cur_loc -= 1
            loc_b[time_b] = cur_loc
    elif d == 'R':
        for _ in range(t):
            time_b += 1
            cur_loc += 1
            loc_b[time_b] = cur_loc
#움직임 종료 후에는 같은 위치에 계속 머물러있음
for i in range(time_b + 1, 1000001):
    loc_b[i] = cur_loc

cnt = 0
if time_a >= time_b:
    for i in range(1, time_a+1):
        if loc_a[i-1] != loc_b[i-1] and loc_a[i] == loc_b[i]:
            cnt += 1
elif time_a <= time_b:
    for i in range(1, time_b+1):
        if loc_a[i-1] != loc_b[i-1] and loc_a[i] == loc_b[i]:
            cnt += 1

print(cnt)