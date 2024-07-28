s = input()

for elem in s:
    if elem.isalpha():
        if elem >= 'A' and elem <= 'Z':
            print(elem, end = "")
        else:
            upper = chr(ord(elem) - ord('a') + ord('A'))
            print(upper, end = '')