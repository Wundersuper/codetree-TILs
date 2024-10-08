N = int(input())

dots = [
    tuple(map(int, input().split()))
    for _ in range(N)
]

max_val = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            x1, y1 = dots[i]
            x2, y2 = dots[j]
            x3, y3 = dots[k]

            if (x1 == x2 or x2 == x3 or x3 == x1) and \
            (y1 == y2 or y2 == y3 or y3 == y1):
                ans = abs((x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3))
                max_val = max(max_val, ans)

print(max_val)