x, y = tuple(map(int, input().split()))

max_sum = 0
for i in range(x, y+1):
    nums = list(map(int, list(str(i))))
    total_sum = sum(nums)

    max_sum = max(max_sum, total_sum)

print(max_sum)