N = int(input())

nums = [
    int(input())
    for _ in range(N)
]

cnt = 1
result = 1
for i in range(1, N):
    if nums[i] == nums[i-1]:
        cnt += 1
    else:
        result = max(cnt, result)
        cnt = 1
    result = max(cnt, result)

print(result)