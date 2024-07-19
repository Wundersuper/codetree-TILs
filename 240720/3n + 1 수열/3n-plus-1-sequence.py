N = int(input())
cnt = 0

while True:
    if N == 1:
        print(cnt)
        break
    if N % 2 == 0:
        cnt += 1
        N //= 2
    else:
        cnt += 1
        N = N * 3 + 1