a, b = map(int, input().split())


def have_num(n):
    while n > 0:
        if n % 10 == 3 or n % 10 == 6 or n % 10 == 9:
            return True
        n = n // 10


def is_magic_number(n):
    return n % 3 == 0 or have_num(n)


cnt = 0
for i in range(a, b+1):
    if is_magic_number(i):
        cnt += 1

print(cnt)