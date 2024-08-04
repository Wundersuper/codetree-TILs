n = int(input())
arr = list(map(int, input().split()))


def lcm(n):
    global arr

    if n == 1:
        return arr[0]
    
    last = lcm(n-1)

    for i in range(arr[n-1], 0, -1):
        if arr[n-1] % i == 0 and last % i == 0:
            return last // i * arr[n-1]


print(lcm(n))