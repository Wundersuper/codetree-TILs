n = int(input())
init = ord('A')

for i in range(n):
    for j in range(n):
        print(chr(init), end = "")
        init += 1
    print()