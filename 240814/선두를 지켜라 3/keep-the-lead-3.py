N, M = tuple(map(int, input().split()))

loc_a, loc_b = [0] * 1000001, [0] * 1000001
first = [0] * 1000001

cur_loc, time = 0, 0
for i in range(N):
    v, t = tuple(map(int, input().split()))

    for j in range(t):
        cur_loc += v
        time += 1
        loc_a[time] = cur_loc

cur_loc, time = 0, 0
for i in range(M):
    v, t = tuple(map(int, input().split()))

    for j in range(t):
        cur_loc += v
        time += 1
        loc_b[time] = cur_loc

for i in range(1, time+1):
    if loc_a[i] > loc_b[i]:
        first[i] = 'a'
    elif loc_a[i] < loc_b[i]:
        first[i] = 'b'
    elif loc_a[i] == loc_b[i]:
        first[i] = 'ab'

cnt = 1
for i in range(2, time+1):
    if first[i-1] != first[i]:
        cnt += 1

print(cnt)