n = int(input())
string = list(input())

cnt = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if string[i] + string[j] + string[k] == 'COW':
                cnt += 1
    
print(cnt)