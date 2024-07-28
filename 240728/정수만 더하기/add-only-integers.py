A = input()

sum_val = 0
for elem in A:
    if elem >= '0' and elem <= '9':
        elem = int(elem)
        sum_val += elem

print(sum_val)