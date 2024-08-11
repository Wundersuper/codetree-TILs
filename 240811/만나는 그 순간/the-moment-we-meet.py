N, M = tuple(map(int, input().split()))

A = []
B = []

loc_a, loc_b = 0, 0
for i in range(N):
    direction, move = tuple(input().split())
    move = int(move)
    if direction == 'L':
        for _ in range(move):
            loc_a -= 1
            A.append(loc_a)
    else:
        for _ in range(move):
            loc_a += 1
            A.append(loc_a)      

for i in range(M):
    direction, move = tuple(input().split())
    move = int(move)
    if direction == 'L':
        for _ in range(move):
            loc_b -= 1
            B.append(loc_b)
    else:
        for _ in range(move):
            loc_b += 1
            B.append(loc_b)

ans = -1
for i in range(1, 1000000):
    if A[i] == B[i]:
        ans = i+1
        break

print(ans)