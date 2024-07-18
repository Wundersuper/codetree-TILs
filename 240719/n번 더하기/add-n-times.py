inp = input()
a = int(inp.split()[0])
n = int(inp.split()[1])

for _ in range(n):
    print(a + n)
    a += n