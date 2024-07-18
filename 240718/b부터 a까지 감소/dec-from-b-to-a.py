n = input()

a = int(n.split()[0])
b = int(n.split()[1])

for i in range(b, a-1, -1):
    print(i, end = " ")