str_a = input()
str_b = input()

lst_a = list(str_a)

while True:
    if len(str_a) >= len(str_b):
        idx = ''.join(lst_a).index(str_b)
        lst_a = lst_a[:idx] + lst_a[idx+2:]
        if str_b not in ''.join(lst_a):
            print(''.join(lst_a))
            break
        else:
            continue
    else:
        print(str_a)
        continue