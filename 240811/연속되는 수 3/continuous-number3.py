N = int(input())

nums = [
    int(input())
    for _ in range(N)
]

ans, cnt = 0, 0

for i in range(N):
    if i >= 1 and (nums[i] * nums[i-1] > 0):
        cnt += 1
    else:
        cnt = 1

    ans = max(ans, cnt)

print(ans)