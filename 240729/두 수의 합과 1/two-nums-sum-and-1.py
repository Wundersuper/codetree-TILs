a, b = map(int, input().split())

ab = str(a + b)

cnt = 0
for elem in ab:
    if elem == '1':
        cnt += 1

print(cnt)