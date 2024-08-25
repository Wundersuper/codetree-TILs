x, y = tuple(map(int, input().split()))

ans = 0
for i in range(x, y+1):
    num = list(map(int, str(i)))
    cnt = [0] * 10
    for n in num:
        cnt[n] += 1
    if cnt.count(1) == 1 and cnt.count(0) == 8:
        ans += 1

print(ans)