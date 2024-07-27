import sys

str1 = input()
str2 = input()

#print(str1.find(str2))
len1 = len(str1)
len2 = len(str2)

for i in range(len1):
    if i + len2 - 1 >= len1:
        continue

    is_matched = True
    for j in range(len2):
        if str1[i+j] != str2[j]:
            is_matched = False
    
    if is_matched:
        print(i)
        sys.exit(0)

print(-1)