arr = input().split()
s, q = arr[0], int(arr[1])

lst = list(s)

for i in range(q):
    qtype, a, b = input().split()

    if qtype == '1':
        str_a = lst[int(a) - 1]
        str_b = lst[int(b) - 1]

        lst[int(a) - 1] = str_b
        lst[int(b) - 1] = str_a
    else:
        for i in range(len(lst)):
            if lst[i] == a:
                lst[i] = b
    
    string = "".join(lst)
    print(string)