n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        print((n + 1 - j) * i, end = " ")
    print()