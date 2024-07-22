arr = list(map(int, input().split()))

for i in range(1, 9):
    arr.append(2 * arr[i-1] + arr[i])

for elem in arr:
    print(elem, end = " ")