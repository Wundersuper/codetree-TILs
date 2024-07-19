cnt = 0
sum_val = 0

while True:
    n = int(input())

    if n >= 20 and n <= 29:
        cnt += 1
        sum_val += n
    else:
        break
    
avg = sum_val / cnt
print(f'{avg:.2f}')