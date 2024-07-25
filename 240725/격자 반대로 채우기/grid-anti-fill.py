n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

cnt = 1
if n % 2 == 0:
    for j in range(n-1, -1, -1):
        if j % 2 != 0:
            for i in range(n-1, -1, -1):
                arr[i][j] = cnt
                cnt += 1
        else:
            for i in range(n):
                arr[i][j] = cnt
                cnt += 1
else:
    for j in range(n-1, -1, -1):
        if j % 2 != 0:
            for i in range(n):
                arr[i][j] = cnt
                cnt += 1
        else:
            for i in range(n-1, -1, -1):
                arr[i][j] = cnt
                cnt += 1

for row in arr:
    for elem in row:
        print(elem, end = " ")
    print()