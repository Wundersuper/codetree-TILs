import sys

N, K = tuple(map(int, input().split()))
basket = [0] * 102

for i in range(N):
    candy, loc = tuple(map(int, input().split()))
    basket[loc] += candy

max_candy = -sys.maxsize
for i in range(102 - 2 * K):
    cnt = 0
    for j in range(i, i + 2 * K + 1):
        cnt += basket[j]
    
    max_candy = max(cnt, max_candy)

print(max_candy)