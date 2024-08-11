n, t = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

ans, cnt = 0, 0
for i in range(n):
    if i >= 1 and nums[i] > t:
        cnt += 1
    else:
        cnt = 0
    
    ans = max(cnt, ans)

print(ans)