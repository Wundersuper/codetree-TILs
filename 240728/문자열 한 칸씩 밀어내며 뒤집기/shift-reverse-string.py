arr = input().split()

s = arr[0]
q = int(arr[1])

for i in range(q):
    inq = input()
    if inq == '1':
        s = s[1:] + s[0]

    elif inq == '2':
        s = s[-1] + s[:-1]

    else:
        s = s[-1] + s[-2] + s[-3] + s[-4]

    print(s)