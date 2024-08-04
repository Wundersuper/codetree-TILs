a, b, c = map(int, input().split())


def sum_all(n):
    if n < 10:
        return n
    
    return sum_all(n // 10) + n % 10

def f(n1, n2, n3):
    result = n1 * n2 * n3

    return sum_all(result)


print(f(a, b, c))