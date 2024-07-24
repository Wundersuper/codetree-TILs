n, m = tuple(map(int, input().split()))

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

cnt = n+m-2
val = 1

for i in range(cnt+1):
    a = 0
    b = i
    for j in range(i+1):
        if (a<n) & (b<m):
            arr[a][b] = val
            val+=1
        a+=1
        b-=1
        
for row in range(n):
    for elem in range(m):
        print(arr[row][elem] , end= " ")
    print()