str1 = input()
str2 = input()
str3 = input()

max_str = len(str1)
min_str = len(str1)

if max_str < len(str2):
    max_str = len(str2)
    if max_str < len(str3):
        max_str = len(str3)

if min_str > len(str2):
    min_str = len(str2)
    if min_str > len(str3):
        min_str = len(str3)

print(max_str - min_str)