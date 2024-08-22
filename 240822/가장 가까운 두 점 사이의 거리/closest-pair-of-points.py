import sys

n = int(input())
dots = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

min_val = sys.maxsize
for i in range(n):
    dist = 0
    for j in range(i+1, n):
        x1, y1 = dots[i]
        x2, y2 = dots[j]

        dist = ((x1 - x2) ** 2) + ((y1 - y2) ** 2) 
        min_val = min(min_val, dist)

print(min_val)