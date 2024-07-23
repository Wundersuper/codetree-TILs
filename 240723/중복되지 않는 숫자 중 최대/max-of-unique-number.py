N = int(input())

arr = list(map(int, input().split()))

max_val = arr[0]

for i in range(1, N):
    if arr[i] > max_val:
        max_val = arr[i]
  
if arr.count(max_val) == 2:
    print(-1)
else:
    print(max_val)