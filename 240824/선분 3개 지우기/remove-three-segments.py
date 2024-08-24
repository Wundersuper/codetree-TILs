n = int(input())
line = [
    tuple(map(int, input().split()))
    for _ in range(n)
]


def is_crossed(a, b, c):
    arr = [0] * 101

    for i in range(n):
        if i == a or i == b or i == c:
            continue
        
        a, b = line[i]
        for dot in range(a, b+1):
            arr[dot] += 1
        
    for i in range(101):
        if arr[i] >= 2:
            return True #겹침
    
    return False


cnt = 1
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if not is_crossed(i, j, k):
                cnt += 1

print(cnt)