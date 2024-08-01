a, b = tuple(map(int, input().split()))


def cond_one(n):
    if n % 2 != 0:
        return cond_two(n)
    else:
        return False
def cond_two(n):
    if n % 10 != 5:
        return cond_three(n)
    else:
        return False

def cond_three(n):
    if n % 3 == 0 and n % 9 != 0:
        return False
    else:
        return True


cnt = 0
for i in range(a, b+1):
    if cond_one(i):
        cnt += 1

print(cnt)