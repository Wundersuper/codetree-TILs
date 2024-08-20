N, M = tuple(map(int, input().split()))
arr_a = list(map(int, input().split())) # N
arr_b = list(map(int, input().split())) # M

cnt = 0
for i in range(N-2):
    part_a = []
    for j in range(i, i+M):
        part_a.append(arr_a[j])
    
    if sorted(part_a) == sorted(arr_b):
        cnt += 1

print(cnt)