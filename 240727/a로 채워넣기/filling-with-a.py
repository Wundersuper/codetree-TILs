str1 = input()

#slicing
#print(str1[0] + 'a' + str1[2:-2] + 'a' + str1[-1])

#list -> join
lst = list(str1)
lst[1], lst[-2] = 'a', 'a'
str2 = ''.join(lst)
print(str2)