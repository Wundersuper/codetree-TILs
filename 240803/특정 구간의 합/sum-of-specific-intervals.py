n, m = tuple(map(int, input().split()))

A = list(map(int, input().split()))


def sum_elem():
    global A
    for i in range(m):
        a, b = tuple(map(int, input().split()))
        sum_val = sum(A[a-1:b])
    
        print(sum_val)


sum_elem()