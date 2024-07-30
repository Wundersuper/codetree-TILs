n, m = tuple(map(int, input().split()))


def lcm(a, b):
    lcm = 1000
    for i in range(1, 1000):
        if i % a == 0 and i % b == 0 and lcm > i:
            lcm = i
    
    print(lcm)

lcm(n, m)