n = input()
a = int(n.split()[0])
b = int(n.split()[1])

for i in range(a, b+1):
    if i % 2 == 1:
        print(i, end = " ")