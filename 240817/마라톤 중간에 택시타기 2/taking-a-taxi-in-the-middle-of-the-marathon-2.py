import sys

INT_MAX = sys.maxsize

N = int(input())
loc = [
    list(map(int, input().split()))
    for _ in range(N)
]

min_val = INT_MAX

for i in range(1, N-1):
    prev_idx = 0
    man_dist = 0
    for j in range(1, N):
        if i == j:
            continue
        man_dist += abs(loc[prev_idx][0]-loc[j][0]) \
                    + abs(loc[prev_idx][1]-loc[j][1])
        prev_idx = j
    
    min_val = min(man_dist, min_val)

print(min_val)