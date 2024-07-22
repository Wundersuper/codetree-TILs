arr = list(map(int, input().split()))

cnt = 0

for elem in arr:
    if elem % 3 == 0:
        break
    cnt += 1

print(arr[cnt-1])