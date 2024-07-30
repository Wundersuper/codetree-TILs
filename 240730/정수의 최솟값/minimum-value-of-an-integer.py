a, b, c = tuple(map(int, input().split()))


def find_min(m, n, s):
    return min(m, n, s)


min_val = find_min(a, b, c)
print(min_val)