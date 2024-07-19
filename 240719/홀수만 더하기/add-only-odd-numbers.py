n = int(input())
sum_val = 0

for i in range(n):
    n = int(input())
    if i % 2 == 1 and i % 3 == 0:
        sum_val += i

print(sum_val)