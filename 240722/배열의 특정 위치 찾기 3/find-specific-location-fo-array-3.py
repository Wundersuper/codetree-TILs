arr = list(map(int, input().split()))

cnt = 0
for elem in arr:
    if elem == 0:
        break
    cnt += 1

print(arr[cnt-1] + arr[cnt-2] + arr[cnt-3])