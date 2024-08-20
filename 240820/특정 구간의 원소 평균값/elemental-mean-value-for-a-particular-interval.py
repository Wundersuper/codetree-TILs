N = int(input())
nums = list(map(int, input().split()))

cnt = 0
for i in range(N):
    for j in range(i, N):
        sum_val, mean_val = 0, 0

        for k in range(i, j+1):
            sum_val += nums[k]
        
        mean_val = sum_val / (j - i + 1)
        exists = False
        for k in range(i, j+1):
            if mean_val == nums[k]:
                exists = True

        if exists:
            cnt += 1

print(cnt)