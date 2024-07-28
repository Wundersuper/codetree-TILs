s = input()

for elem in s:
    if elem >= 'A' and elem <= 'Z':
        print(chr(ord(elem) - ord('A') + ord('a')), end = '')
    else:
        print(chr(ord(elem) - ord('a') + ord('A')), end = '')