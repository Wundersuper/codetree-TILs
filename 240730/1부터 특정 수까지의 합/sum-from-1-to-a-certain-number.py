N = int(input())


def div(a):
    sum_val = 0
    for i in range(1, a+1):
        sum_val += i
    return sum_val // 10


result = div(N)
print(result)