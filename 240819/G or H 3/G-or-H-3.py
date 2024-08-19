import sys

N, K = tuple(map(int, input().split()))

line = [0] * 10001

for i in range(N):
    loc, s = input().split()
    if s == 'G':
        line[int(loc)] = 1
    elif s == 'H':
        line[int(loc)] = 2

max_score = -sys.maxsize
for i in range(1, len(line) - K):
    score = 0
    for j in range(i, i+K+1):
        score += line[j]
    
    max_score = max(max_score, score)

print(max_score)