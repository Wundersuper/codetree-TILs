n, m = tuple(map(int, input().split()))


def common_div(a, b):
    div = 1
    if a >= b:
        for i in range(1, b+1):
            if a % i == 0 and b % i == 0 and div < i:
                div = i
    else:
        for i in range(1, a+1):
            if a % i == 0 and b % i == 0 and div < i:
                div = i
    print(div)

common_div(n, m)