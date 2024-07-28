a, b= input().split()

print(ord(a) + ord(b), end = ' ')
if ord(a) > ord(b):
    print(ord(a) - ord(b))
else:
    print(ord(b) - ord(a))