N, k = tuple(map(int, input().split()))

nums = list(map(int, input().split()))

nums.sort()

print(nums[k-1])