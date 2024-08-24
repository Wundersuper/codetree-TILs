n = int(input())
line = [
    list(map(int, input().split()))
    for _ in range(n)
]


def is_crossed(a, b, c):
    arr = [0] * 101

    for i in range(n):
        if i == a or i == b or i == c:
            continue
        
        for y in range(line[i][0], line[i][1]+1):
            arr[y] += 1
        
    for i in range(101):
        if arr[i] >= 2:
            return True #겹침
    
    return False


cnt = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if not is_crossed(i, j, k):
                cnt += 1

print(cnt)