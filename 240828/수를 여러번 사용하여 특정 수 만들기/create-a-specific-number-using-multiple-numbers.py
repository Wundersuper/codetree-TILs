a, b, c = tuple(map(int, input().split()))

num = 0
ans = -1

for i in range(1001):
    num = 0
    for j in range(1001):
        num = a * i + b * j

        if num <= c:
            ans = max(ans, num)

print(ans)