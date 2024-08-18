n = int(input())
nums = [int(input()) for _ in range(n)]


def carry(a, b, c):
    if (a % 10 + b % 10 + c % 10) > 9:
        return False
    if a == 0 and b == 0 and c == 0:
        return True
    return carry(a // 10, b // 10, c // 10)


ans = -1
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if carry(nums[i], nums[j], nums[k]):
                sum_val = nums[i] + nums[j] + nums[k]
                ans = max(ans, sum_val)

print(ans)