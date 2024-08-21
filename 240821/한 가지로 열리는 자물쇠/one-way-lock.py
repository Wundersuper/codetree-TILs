N = int(input())
arr = list(map(int, input().split()))


total = N*N*N
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            exists = True
            if abs(arr[0] - i) > 2 and abs(arr[1] - j) > 2 and abs(arr[2] - k) > 2:
                exists = False
            
            if not exists:
                total -= 1

print(total)