N, M = tuple(map(int, input().split()))

loc_a = [0] * 1000000
loc_b = [0] * 1000000
first = [0] * 1000000

cur_loc, time = 0, 0
for i in range(N):
    v, t = tuple(map(int, input().split()))

    for _ in range(t):
        cur_loc += v
        time += 1
        loc_a[time] = cur_loc
    
cur_loc, time = 0, 0
for i in range(M):
    v, t = tuple(map(int, input().split()))

    for _ in range(t):
        cur_loc += v
        time += 1
        loc_b[time] = cur_loc

for i in range(1, time+1):
    if loc_a[i] > loc_b[i]:
        first[i] = 1
    elif loc_a[i] < loc_b[i]:
        first[i] = 2
    elif loc_a[i] == loc_b[i]:
        first[i] = first[i-1]

cnt = 0
for i in range(2, time+1):
    if first[i-1] > 0 and first[i] != first[i-1]:
        cnt += 1

print(cnt)