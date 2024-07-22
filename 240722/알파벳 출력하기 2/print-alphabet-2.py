n = int(input())
init = ord('A')

for i in range(n):
    for j in range(i):
        print(' ', end = " ")

    for j in range(n-i):
        print(chr(init), end = " ")
        init += 1

        if init > ord('Z'):
            init = ord('A')

    print()