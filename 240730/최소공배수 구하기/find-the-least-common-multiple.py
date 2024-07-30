n, m = tuple(map(int, input().split()))


def lcm(a, b):
    for i in range(1, 500):
        if i % a == 0 and i % b == 0:
            lcm = i
            break
    
    print(lcm)

lcm(n, m)