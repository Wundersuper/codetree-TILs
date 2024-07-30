n, m = tuple(map(int, input().split()))


def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            lcm = i
            break
    print(lcm)
        

lcm(n, m)