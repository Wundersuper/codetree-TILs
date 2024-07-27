str1 = input()
lst = list(str1)

#for i in range(len(lst)):
#    if lst[i] == lst[0]:
#        lst[i] = lst[1]
#    if lst[i] == lst[1]:
#        lst[i] = lst[0]

#re_str = ''.join(lst)
#print(re_str)


str2 = str1.replace('c', 'o')

print(str2[0] + 'c' + str2[2:])