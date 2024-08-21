import sys

N = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

min_val = sys.maxsize
for i in range(N):
    xs, ys = [], []
    for j in range(N):
        if i == j:
            continue
        
        xs.append(arr[j][0])
        ys.append(arr[j][1])

    ans = abs(max(xs) - min(xs)) * abs(max(ys) - min(ys))
    min_val = min(min_val, ans)

print(ans)