n = int(input())

sum_val = 0
for i in range(n):
    x = int(input())

    sum_val += x

sum_val = str(sum_val)
result = sum_val[1:] + sum_val[0]

print(result)