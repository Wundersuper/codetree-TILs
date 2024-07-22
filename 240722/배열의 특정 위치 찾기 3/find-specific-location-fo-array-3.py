arr = list(map(int, input().split()))

sum_val = 0
for elem in arr:
    if elem == 0:
        break
    sum_val += elem

print(sum_val)