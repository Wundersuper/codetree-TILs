import sys

INT_MAX = sys.maxsize

N = int(input())
nums = [int(input()) for _ in range(N)]

min_val = INT_MAX
for i in range(N):
    sum_val = 0
    for j in range(N):
        if j >= i:
            sum_val += nums[j] * abs(j-i)
        else:
            sum_val += nums[j] * abs(j-i+N)
    
    min_val = min(min_val, sum_val)

print(min_val)