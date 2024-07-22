n = int(input())
init = ord('A')

for i in range(n):
    for j in range(i+1):
        print(chr(init), end = "")
        init += 1
    print()