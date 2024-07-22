n = int(input())

arr = [1, n]

for i in range(1, 100):
    if arr[i] > 100:
        break
    arr.append(arr[i-1] + arr[i])

for elem in arr:
    print(elem, end = " ")