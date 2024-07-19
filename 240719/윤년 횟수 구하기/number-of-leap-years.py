n = int(input())
cnt1, cnt2 = 0, 0

for i in range(1, n+1):
    if i % 4 == 0:
        if i % 100 == 0 and i % 400 != 0:
            cnt2 += 1
        else:
            cnt1 += 1
    else:
        cnt2 += 1

print(cnt1)