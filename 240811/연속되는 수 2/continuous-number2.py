N = int(input())

nums = [
    int(input())
    for _ in range(N)
]

index = []
for i in range(N):
    if i == 0 or nums[i] != nums[i-1]:
        index.append(i)

maxval = 0
for i in range(1, len(index)):
    cnt = index[i] - index[i-1]
    if maxval < cnt:
        maxval = cnt

print(maxval)