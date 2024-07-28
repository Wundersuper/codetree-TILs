s = input()

for elem in s:
    if elem.isalpha() or elem.isdigit():
        if elem >= 'A' and elem <= 'Z':
            print(chr(ord(elem) - ord('A') + ord('a')), end = "")
        else:
            print(elem, end = "")