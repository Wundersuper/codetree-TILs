a, b = tuple(map(int, input().split()))


def two_int(m, n):
    if m > n:
        m += 25
        n *= 2
    else:
        n += 25
        m *= 2
    
    return m, n


a, b = two_int(a, b)
print(a, b)