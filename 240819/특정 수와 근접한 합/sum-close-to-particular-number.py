N, S = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

total_sum = sum(nums)

min_val = 100
for i in range(N-1):
    for j in range(i+1, N):
        sum_val = total_sum - (nums[i] + nums[j])
        diff = abs(S - sum_val)

        min_val = min(min_val, diff)

print(min_val)