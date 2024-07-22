n = int(input())

for i in range(1, n+1):
    sum_val = 0
    for j in range(1, i+1):
        if i % j == 0:
            sum_val += 1
    
    if sum_val == 2:
        print(i, end = " ")