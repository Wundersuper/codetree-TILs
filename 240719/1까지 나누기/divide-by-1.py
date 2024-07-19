n = int(input())

cnt = 0

for i in range(1, n):
    cnt += 1
    quo = n // i
    if quo > 1:
        n = quo
        continue
    else:
        break

print(cnt)