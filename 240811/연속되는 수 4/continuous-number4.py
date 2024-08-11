N = int(input())

nums = [
    int(input())
    for _ in range(N)
]

ans, cnt = 0, 0
for i in range(N):
    if i >= 1 and nums[i-1] < nums[i]:
        cnt += 1
    else:
        cnt = 1
    ans = max(cnt, ans)

print(ans)