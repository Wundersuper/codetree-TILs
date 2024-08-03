n, m = tuple(map(int, input().split()))

A = list(map(int, input().split()))


def sum_elem():
    global m
    sum_val = 0
    
    while m >= 1:
        sum_val += A[m - 1]
        if m % 2 != 0:
            m -= 1
        else:
            m //= 2
    
    return sum_val


print(sum_elem())