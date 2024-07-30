def find_x(a):
    return a % 2 == 0 and (a // 10 + a % 10) % 5 == 0


n = int(input())

if find_x(n):
    print('Yes')
else:
    print('No')