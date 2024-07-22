start, end = map(int, input().split())
cnt = 0

for i in range(start, end+1):
    sum_val = 0
    for j in range(1, i+1):
        if i % j == 0:
            sum_val += 1
    
    if sum_val == 3:
        cnt += 1

print(cnt)