n = int(input())
height = [int(input()) for _ in range(n)]


def iceberg(x):
    curr_cnt = 0
    if height[0] > x:
        curr_cnt += 1
    for i in range(1, n):
        if height[i-1] <= x and height[i] > x:
            curr_cnt += 1
    return curr_cnt


ans = -1
for i in range(1, 1001):
    ans = max(ans, iceberg(i))

print(ans)