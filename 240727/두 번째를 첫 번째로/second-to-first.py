s = input()

lst_s = list(s)

a = lst_s[1]
b = lst_s[0]

for i in range(len(lst_s)):
    if lst_s[i] == a:
        lst_s[i] = b

result = ''.join(lst_s)
print(result)