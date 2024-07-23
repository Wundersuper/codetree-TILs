import sys
N = int(input())

arr = list(map(int, input().split()))

max_val = -sys.maxsize

for i in range(1, N):
    if arr[i] > max_val:
        max_val = arr[i]
    
    if arr.count(max_val) >= 2:
        max_val = -sys.maxsize

if max_val in arr:
    print(max_val)
else:
    print(-1)