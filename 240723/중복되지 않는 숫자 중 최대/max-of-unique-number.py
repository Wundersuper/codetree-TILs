N = int(input())

arr = list(map(int, input().split()))

max_val = 0
nn = []

for i in range(N):
    if arr[i] in nn:
        continue
    
    if arr[i] in arr[i+1:]:
        nn.append(arr[i])
        continue

    if arr[i] > max_val:
        max_val = arr[i]

if max_val == 0:
    print(-1)
else:
    print(max_val)