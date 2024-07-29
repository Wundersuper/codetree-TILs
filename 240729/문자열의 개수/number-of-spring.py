cnt = 0
lst = []

for i in range(200):
    s = input()

    if s == '0':
        print(cnt)
        for i in range(0, len(lst), 2):
            print(lst[i])
        break
    
    cnt += 1
    lst.append(s)