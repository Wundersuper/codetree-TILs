n = int(input())

for i in range(n):
    if i == 0 or i == (n - 1):
        for j in range(n):
            print('*', end = " ")
    else:
        for j in range(i+1):
            print('*', end =" ")
    print()