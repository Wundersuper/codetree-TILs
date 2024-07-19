while True:
    inp = input()
    a, b, c = int(inp.split()[0]), int(inp.split()[1]), inp.split()[2]

    print(a * b)

    if c == 'C':
        break