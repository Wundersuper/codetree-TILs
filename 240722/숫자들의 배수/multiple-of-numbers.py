n = int(input())

cnt = 0

for i in range(1, 11):
    if (n * i) % 5 == 0:
        cnt += 1
    
    if cnt > 2:
        break

    print(f'{n * i}', end = " ")