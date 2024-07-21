n = int(input())
sum_val = 2

for i in range(n):
    for j in range(n):
        if sum_val >= 10:
            sum_val = 2
        print(sum_val, end = " ")
        sum_val += 2
    print()