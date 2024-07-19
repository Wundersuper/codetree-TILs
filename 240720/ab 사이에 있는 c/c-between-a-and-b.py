a, b, c = map(int, input().split())
multiple = False

for i in range(a, b+1):
    if i % c == 0:
        multiple = True

if multiple == True:
    print('YES')
else:
    print('NO')