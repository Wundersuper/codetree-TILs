import sys

INT_MIN = -sys.maxsize

n = int(input())
nums = list(map(int, input().split()))

max_val = INT_MIN
sum_val = 0
for i in range(n):
    for j in range(i+2, n):
        sum_val = nums[i] + nums[j]
        max_val = max(sum_val, max_val)

print(max_val)