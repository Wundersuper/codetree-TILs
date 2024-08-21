import sys

arr = list(map(int, input().split()))


def get_diff(x, y, z):
    sum1 = arr[x] + arr[y] + arr[z]
    sum2 = sum(arr) - sum1
    return abs(sum1 - sum2)


min_diff = sys.maxsize
for i in range(6):
    for j in range(i+1, 6):
        for k in range(j+1, 6):
            min_diff = min(min_diff, get_diff(i, j, k))

print(min_diff)