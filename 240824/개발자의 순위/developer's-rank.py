k, n = tuple(map(int, input().split()))
rank = [
    list(map(int, input().split()))
    for _ in range(k)
]


def is_pair(a, b):
    for i in range(1, k):
        for j in range(n):
            if rank[i][j] == a:
                rank_a = j
            elif rank[i][j] == b:
                rank_b = j
            
        if rank_a > rank_b:
            return False
    
    return True

cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        if is_pair(rank[0][i], rank[0][j]):
            cnt += 1

print(cnt)