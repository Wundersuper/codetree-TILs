import sys

score = list(map(int, input().split()))
sort = sorted(score)

result = []
n = 6
for i in range(n // 2):
    result.append(sort[i] + sort[-i-1])

result.sort()
print(result[-1] - result[0])