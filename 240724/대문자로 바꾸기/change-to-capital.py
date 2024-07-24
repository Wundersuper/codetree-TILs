arr = [
    list(input().split())
    for _ in range(5)
]

for i in range(5):
    for j in range(3):
        arr[i][j] = chr(ord(arr[i][j]) + (ord('A') - ord('a')))

        print(arr[i][j], end = " ")
    print()