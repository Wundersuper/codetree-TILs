N, K = tuple(map(int, input().split()))
blocks = [0 for _ in range(N+1)]

for i in range(K):
    a, b = tuple(map(int, input().split()))

    for j in range(a, b+1):
        blocks[j-1] += 1

print(max(blocks))