a, b = tuple(map(int, input().split()))


def two_int(m, n):
    if m > n:
        n += 10
        m *= 2
    else:
        m += 10
        n *= 2
    return m, n


a, b = two_int(a, b)
print(a, b)