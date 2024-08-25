n, c, g, h = tuple(map(int, input().split()))
temp = [
    tuple(map(int, input().split()))
    for _ in range(n)
]


def find_temp(num, a, b):
    if num < a:
        return c
    elif num >= a and num <= b:
        return g
    elif num > b:
        return h


ans = 0
for i in range(1001):
    capacity = 0
    for j in range(n):
        ta, tb = temp[j]
        capacity += find_temp(i, ta, tb)
    
    ans = max(ans, capacity)

print(ans)