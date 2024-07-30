n, m = tuple(map(int, input().split()))


def lcm(a, b):
    for i in range(1, 500):
        if i % a == 0 and i % b == 0:
            min_val = i
            break
    
    print(min_val)

lcm(n, m)