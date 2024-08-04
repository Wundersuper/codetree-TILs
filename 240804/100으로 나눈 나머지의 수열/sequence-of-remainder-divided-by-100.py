N = int(input())


def func(n):
    if n == 1:
        return 2
    if n == 2:
        return 4
    
    return (func(n-2) * func(n-1)) % 100


print(func(N))