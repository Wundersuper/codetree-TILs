n = int(input())
nums = list(map(int, input().split()))

max_cnt = 0
for k in range(1, 101):
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if (nums[j] - k) == (k - nums[i]):
                cnt += 1
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)