n = input()
mid = int(n.split()[0])
fin = int(n.split()[1])

if mid >= 90 and fin >= 95:
    print(100000)
elif mid >= 90 and fin >= 90:
    print(50000)
else:
    print(0)