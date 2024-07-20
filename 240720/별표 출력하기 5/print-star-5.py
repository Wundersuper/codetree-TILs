n = int(input())

for i in range(n, 0, -1):
    print('*' * i, end = " ")
    for _ in range(i-1):
            print('*' * i, end = " ")
    print()