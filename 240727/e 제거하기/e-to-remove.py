string = input()

lst = list(string)
leng = len(lst)

for i in range(leng):
    if lst[i] == 'e':
        lst = lst[:i] + lst[i+1:]
        print(''.join(lst))
        break