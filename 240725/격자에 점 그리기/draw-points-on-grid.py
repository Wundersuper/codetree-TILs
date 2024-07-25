n, m = tuple(map(int, input().split()))

arr = [
    [0 for _ in range(10)]
    for _ in range(10)
]

#입력된 순서 표기
for i in range(1, m+1):
    r, c = tuple(map(int, input().split()))
    arr[r][c] = i

for i in range(1, n+1):
    for j in range(1, n+1):
        print(arr[i][j], end = " ")
    print()