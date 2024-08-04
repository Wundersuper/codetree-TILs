n = int(input())


def f(m):
    if m == 1:
        return 0
    
    if m % 2 == 0:
        return f(m // 2) + 1
    else:
        return f(m * 3 + 1) + 1


print(f(n))