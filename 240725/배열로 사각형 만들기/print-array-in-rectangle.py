arr = [
    [0 for _ in range(5)]
    for _ in range(5)
]

for i in range(5):
    arr[i][0] = 1

for j in range(5):
    arr[0][j] = 1

for i in range(1, 5):
    for j in range(1, 5):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

for row in arr:
    for elem in row:
        print(elem, end = " ")
    print()