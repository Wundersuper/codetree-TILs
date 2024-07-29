s1 = input()
s2 = input()

new1 = ''
new2 = ''

for elem in s1:
    if elem >= '0' and elem <= '9':
        new1 += elem

for elem in s2:
    if elem >= '0' and elem <= '9':
        new2 += elem

print(int(new1) + int(new2))