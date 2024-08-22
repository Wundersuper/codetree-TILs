import sys

n = int(input())
dots = [
    list(map(int, input().split()))
    for _ in range(n)
]

min_val = sys.maxsize
for i in range(n):
    dist = 0
    xs, ys = [], []
    for j in range(n):
        for k in range(n):
            if i == j or k == i or k == j:
                continue
            
            xs.append(dots[j][0])
            xs.append(dots[k][0])
            ys.append(dots[j][1])
            ys.append(dots[k][1])

            dist = ((xs[0] - xs[1]) ** 2) + ((ys[0] - ys[1]) ** 2) 
            min_val = min(min_val, dist)

print(min_val)