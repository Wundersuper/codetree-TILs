A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = list(map(int, input().split()))

tile = [[0]*2000 for _ in range(2001)]
OFFSET = 1000

for i in range(len(A)):
    A[i] += OFFSET

for i in range(len(B)):
    B[i] += OFFSET

for i in range(len(M)):
    M[i] += OFFSET

#직사각형 A
for x in range(A[0], A[2]):
    for y in range(A[1], A[3]):
        tile[x][y] += 1
#직사각형 B
for x in range(B[0], B[2]):
    for y in range(B[1], B[3]):
        tile[x][y] += 1
#직사각형 M
for x in range(M[0], M[2]):
    for y in range(M[1], M[3]):
        tile[x][y] -= 1

area = 0
for x in range(min(A[0], B[0]), max(A[2], B[2])):
    for y in range(min(A[1], B[1]), max(A[3], B[3])):
        if tile[x][y] == 1:
            area += 1

print(area)