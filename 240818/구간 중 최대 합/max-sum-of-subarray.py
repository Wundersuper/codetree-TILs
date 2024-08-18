import sys

INT_MIN = -sys.maxsize

n, k = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

max_val = INT_MIN
for i in range(n-k+1):
    sum_val = 0
    for j in range(k):
        sum_val += nums[i + j]
        max_val = max(max_val, sum_val)

print(max_val)