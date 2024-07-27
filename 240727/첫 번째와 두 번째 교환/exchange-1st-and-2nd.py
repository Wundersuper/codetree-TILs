str1 = input()
str2 = str1
lst1 = list(str1)
lst2 = list(str2)

for i in range(len(lst1)):
    if lst1[i] == lst2[0]:
        lst1[i] = lst2[1]
    elif lst1[i] == lst2[1]:
        lst1[i] = lst2[0]

result = ''.join(lst1)
print(result)